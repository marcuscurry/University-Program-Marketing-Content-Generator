import ollama
from marketing_generator.prompts import get_system_prompt_brochure, get_system_prompt_student

def get_links_ollama(messages):
    """
    messages: list[dict] => [{"role": "system", ...}, {"role": "user", ...}]
    Returns parsed JSON (ollama already formats when format='json').
    """
    response = ollama.chat(
        model="llama3.2",
        messages=messages,
        format="json",
    )
    # response.message.content is already JSON text; caller loads it
    return response.message.content


def ollama_brochure(user_prompt: str, major: str) -> str:
    sp = get_system_prompt_brochure(major)
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {"role": "system", "content": sp},
            {"role": "user", "content": user_prompt},
        ],
    )
    return response.message.content


def judge_brochures(user_prompt_student: str, major: str) -> str:
    sp = get_system_prompt_student(major)
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {"role": "system", "content": sp},
            {"role": "user", "content": user_prompt_student},
        ],
        stream=False,
    )
    return response.message.content
