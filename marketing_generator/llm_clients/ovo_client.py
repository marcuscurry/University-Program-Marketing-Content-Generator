import json
from openai import OpenAI
from marketing_generator.prompts import system_prompt_brochure


def get_links_ollama_via_openai(messages):
    """
    Uses OpenAI-compatible interface against local Ollama server.
    Returns parsed JSON.
    """
    ollama_via_openai = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
    response = ollama_via_openai.chat.completions.create(
        model="llama3.2",
        messages=messages,
        response_format={"type": "json_object"},
    )
    result = response.choices[0].message.content
    return json.loads(result)


def ovo_brochure(user_prompt: str) -> str:
    ollama_via_openai = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
    response = ollama_via_openai.chat.completions.create(
        model="llama3.2",
        messages=[
            {"role": "system", "content": system_prompt_brochure},
            {"role": "user", "content": user_prompt},
        ],
    )
    return response.choices[0].message.content
