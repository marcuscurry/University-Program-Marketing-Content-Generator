import gradio as gr
from marketing_generator.brochure import create_brochure
from marketing_generator.evaluate import rank_brochures

def generate_ui_brochure(subject, url, api_choice):
    brochure = create_brochure(subject, url, api_choice)
    return brochure, brochure, "✅ Done!"

def rank_ui_brochures(uw, ut, uc):
    return rank_brochures(ut, uc, uw)

with gr.Blocks() as demo:
    gr.Markdown("# 🎓 University Program Marketing Generator")

    with gr.Row():
        subject = gr.Textbox(label="Program Name", value="University of Washington MSDS")
        url = gr.Textbox(label="Program URL", value="https://www.washington.edu/datasciencemasters/")
        api_choice = gr.Dropdown(
            choices=[
                ("gpt-4o-mini", "a"),
                ("Llama3.2", "b"),
                ("Llama3.2 via OpenAI", "c"),
                ("Claude-haiku", "d")
            ],
            label="LLM",
            value=None,
            allow_custom_value=False,
            interactive=True
        )

    generate_button = gr.Button("Generate Brochure")
    status_label = gr.Label(value="")

    with gr.Tabs():
        with gr.Tab("Markdown View"):
            markdown_output = gr.Markdown()
        with gr.Tab("Raw Text View"):
            raw_output = gr.Textbox(lines=20)

    generate_button.click(
        fn=generate_ui_brochure,
        inputs=[subject, url, api_choice],
        outputs=[raw_output, markdown_output, status_label]
    )

    gr.Markdown("## 🧠 Compare 3 Brochures")

    uw_input = gr.Textbox(label="UW Brochure", lines=10)
    ut_input = gr.Textbox(label="UT Brochure", lines=10)
    uc_input = gr.Textbox(label="UChicago Brochure", lines=10)
    rank_button = gr.Button("Rank Programs")

    ranking_output = gr.Textbox(label="Ranking Output", lines=10)
    rank_button.click(
        fn=rank_ui_brochures,
        inputs=[uw_input, ut_input, uc_input],
        outputs=ranking_output
    )

demo.launch()
