from cProfile import label

import gradio as gr
from marketing_generator.brochure import create_brochure
from marketing_generator.evaluate import rank_brochures
from marketing_generator.db import fetch_majors, fetch_programs_by_major, get_program_by_id

# ------------------------
# Brochure Generation Logic
# ------------------------

# For storing brochures generated through the UI
generated_brochures = {}

def generate_ui_brochure(program_id, api_choice):
    subject, url, major = get_program_by_id(program_id)
    brochure = create_brochure(subject, url, api_choice, major)

    # Cache it
    generated_brochures[program_id] = {
        "subject": subject,
        "brochure": brochure,
        "major": major
    }

    return brochure, brochure, f"✅ Brochure Completed for: {subject} ✅"


# ------------------------
# Brochure Ranking Logic
# ------------------------

def get_cached_brochure_options():
    return [(data["subject"], pid) for pid, data in generated_brochures.items()]

def refresh_brochure_dropdowns():
    options = get_cached_brochure_options()
    return (
        gr.update(choices=options, value=None),
        gr.update(choices=options, value=None),
        gr.update(choices=options, value=None),
    )

def rank_ui_brochures(pid1, pid2, pid3):
    try:
        b1 = generated_brochures[pid1]["brochure"]
        b2 = generated_brochures[pid2]["brochure"]
        b3 = generated_brochures[pid3]["brochure"]
        major = generated_brochures[pid1].get("major", "General")
        return rank_brochures(b1, b2, b3, major)
    except KeyError as e:
        return f"❌ Missing brochure for Program ID: {e}"


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

    generate_click_event = generate_button.click(
        fn=generate_ui_brochure,
        inputs=[program_dropdown, api_choice],
        outputs=[raw_output, markdown_output, status_label]
    )

    # -------- Ranking Section --------
    gr.Markdown("## 🧠 Compare & Rank Brochures")

    with gr.Row():
        pid1 = gr.Dropdown(label="🏫 Program 1", choices=[], interactive=True)
        pid2 = gr.Dropdown(label="🏫 Program 2", choices=[], interactive=True)
        pid3 = gr.Dropdown(label="🏫 Program 3", choices=[], interactive=True)

        criteria = gr.Textbox(label="Important criteria to be taken into account for the programs:", lines=4, interactive=True)

    # Attach the refresh after dropdowns are defined
    generate_click_event.then(
        fn=refresh_brochure_dropdowns,
        inputs=[],
        outputs=[pid1, pid2, pid3]
    )

    demo.load(
        fn=refresh_brochure_dropdowns,
        inputs=[],
        outputs=[pid1, pid2, pid3]
    )

    rank_button = gr.Button("📊 Rank Programs")
    ranking_output = gr.Markdown(label="🏆 Program Ranking Result")
    status_label = gr.Label(value="", label="Status")

    rank_button.click(
        fn=rank_ui_brochures,
        inputs=[pid1, pid2, pid3],
        outputs=[ranking_output, status_label]
    )


# ------------------------
# Launch UI
# ------------------------

demo.launch()
