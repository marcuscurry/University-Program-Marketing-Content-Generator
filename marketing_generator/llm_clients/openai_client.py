import json
from openai import OpenAI
from IPython.display import Markdown, display, update_display  # used by stream helper
from marketing_generator.config import OPENAI_MODEL  # relative import from package root
from marketing_generator.prompts import get_system_prompt_brochure  # stream uses this prompt


def get_links_openai(messages):
    """
    messages: list[dict] => [{"role": "system", ...}, {"role": "user", ...}]
    Returns parsed JSON from OpenAI response.
    """
    client = OpenAI()
    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=messages,
        response_format={"type": "json_object"},
    )
    result = response.choices[0].message.content
    return json.loads(result)


def openai_brochure(user_prompt: str, major: str) -> str:
    client = OpenAI()
    sp = get_system_prompt_brochure(major)
    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[
            {"role": "system", "content": sp},
            {"role": "user", "content": user_prompt},
        ],
        stream=False,
    )
    return response.choices[0].message.content


def openai_stream_brochure(user_prompt: str, major: str):
    """Streams markdown back via IPython display."""
    client = OpenAI()
    sp = get_system_prompt_brochure(major)
    stream = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[
            {"role": "system", "content": sp},
            {"role": "user", "content": user_prompt},
        ],
        stream=True,
    )

    response = ""
    display_handle = display(Markdown(""), display_id=True)
    for chunk in stream:
        response += chunk.choices[0].delta.content or ""
        response = response.replace("```", "").replace("markdown", "")
        update_display(Markdown(response), display_id=display_handle.display_id)
