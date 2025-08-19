import json
from marketing_generator.scraping import Webpage
from .llm_clients.anthropic_client import get_links_claude
from .prompts import system_prompt_links
from .llm_clients.openai_client import get_links_openai
from .llm_clients.ollama_client import get_links_ollama
from .llm_clients.ovo_client import get_links_ollama_via_openai


def get_links_user_prompt(website: Webpage) -> str:
    user_prompt = f"Here is the list of links on the website of {website.url} - "
    user_prompt += (
        "please decide which of these are relevant web links for a brochure about the company, "
        "respond with the full https URL in JSON format. Do not include Terms of Service, Privacy, email links.\n"
    )
    user_prompt += "Links (some might be relative links):\n"
    user_prompt += "\n".join(website.links)
    return user_prompt


def get_messages(url: str):
    user_prompt_links = get_links_user_prompt(Webpage(url))
    return [
        {"role": "system", "content": system_prompt_links},
        {"role": "user", "content": user_prompt_links},
    ]


def api_call(url: str, api: str):
    messages = get_messages(url)
    if (api.lower() == "a") or (api.lower() == "openai"):
        return get_links_openai(messages)
    elif (api.lower() == "b") or (api.lower() == "ollama"):
        result_json = get_links_ollama(messages)
        return json.loads(result_json)
    elif (api.lower() == "c") or (api.lower() == "ollama via openai"):
        return get_links_ollama_via_openai(messages)
    elif (api.lower() == "d") or (api.lower() == "claude"):
        return get_links_claude(messages[0]['content'],[messages[1]])
    else:
        raise ValueError("Unknown API choice. Use A, B, C, or D.")
