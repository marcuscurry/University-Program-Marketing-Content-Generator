import gradio as gr
from marketing_generator.brochure import create_brochure
from marketing_generator.evaluate import rank_brochures
from marketing_generator.db import fetch_majors, fetch_programs_by_major, get_program_by_id

# ------------------------
# Brochure Generation Logic
# ------------------------
def generate_ui_brochure(program_id, api_choice):
    # get selected program data from db
    subject, url = get_program_by_id(program_id)
    brochure = create_brochure(subject, url, api_choice)
    return brochure, brochure, "✅ Brochure Completed!"

# ------------------------
# Brochure Ranking Logic
# ------------------------
def rank_ui_brochures(uw, ut, uc):
    return rank_brochures(ut, uc, uw)

# ------------------------
# Dynamic Dropdown Loaders
# ------------------------
def load_programs_by_major(major_id):
    programs = fetch_programs_by_major(major_id)
    return gr.update(choices=[(name, pid) for pid, name in programs], value=None)

# ------------------------
# UI Construction
# ------------------------
with gr.Blocks() as demo:
    gr.Markdown("# 🎓 University Program Marketing Generator")

    # -------- Brochure Section --------
    gr.Markdown("## ✨ Generate Program Brochure")

    with gr.Row():
        majors = fetch_majors()
        major_dropdown = gr.Dropdown(
            choices=[(name, id) for id, name in majors],
            label="🎓 Select Major",
            value=None,
            interactive=True
        )

        program_dropdown = gr.Dropdown(
            label="🏫 Select Program",
            interactive=True
        )

        api_choice = gr.Dropdown(
            choices=[
                ("gpt-4o-mini", "a"),
                ("Llama3.2", "b"),
                ("Llama3.2 via OpenAI", "c"),
                ("Claude-haiku", "d")
            ],
            label="LLM Model",
            value=None,
            interactive=True
        )

    major_dropdown.change(
        fn=load_programs_by_major,
        inputs=major_dropdown,
        outputs=program_dropdown
    )

    generate_button = gr.Button("🚀 Generate Brochure")
    status_label = gr.Label(value="", label="Status")

    gr.Markdown("### 📝 Brochure Output")
    with gr.Tabs():
        with gr.Tab("📄 Markdown View"):
            markdown_output = gr.Markdown()
        with gr.Tab("📃 Raw Text View"):
            raw_output = gr.Textbox(lines=20, label="Brochure Text")

    generate_button.click(
        fn=generate_ui_brochure,
        inputs=[program_dropdown, api_choice],
        outputs=[raw_output, markdown_output, status_label]
    )

    # -------- Ranking Section --------
    gr.Markdown("## 🧠 Compare & Rank Brochures")

    with gr.Row():
        uw_input = gr.Textbox(label="🏫 UW Brochure", lines=6, placeholder="Paste brochure text here...")
        ut_input = gr.Textbox(label="🏫 UT Brochure", lines=6, placeholder="Paste brochure text here...")
        uc_input = gr.Textbox(label="🏫 UChicago Brochure", lines=6, placeholder="Paste brochure text here...")

    rank_button = gr.Button("📊 Rank Programs")
    ranking_output = gr.Textbox(label="🏆 Program Ranking Result", lines=4, interactive=False)

    rank_button.click(
        fn=rank_ui_brochures,
        inputs=[uw_input, ut_input, uc_input],
        outputs=ranking_output
    )

# ------------------------
# Launch UI
# ------------------------
demo.launch()
