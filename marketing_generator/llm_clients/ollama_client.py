import ollama
from marketing_generator.prompts import system_prompt_student


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


def ollama_brochure(user_prompt: str) -> str:
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {"role": "system", "content": (
                "You are an assistant that analyzes the contents of several relevant pages from a "
                "University Degree Program website and creates a short brochure/marketing summary "
                "about the Program for prospective students, partnerships and companies. "
                "Respond in markdown. Include details of University culture, academic benefits and "
                "prospective careers/jobs if you have the information."
            )},
            {"role": "user", "content": user_prompt},
        ],
    )
    return response.message.content


def judge_brochures(user_prompt_student: str) -> str:
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {"role": "system", "content": system_prompt_student},
            {"role": "user", "content": user_prompt_student},
        ],
        stream=False,
    )
    return response.message.content
