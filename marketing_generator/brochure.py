from .aggregator import get_all_details
from .llm_clients.anthropic_client import claude_brochure
from .prompts import get_system_prompt_brochure  # noqa: F401 (kept for clarity)
from .llm_clients.openai_client import openai_brochure, openai_stream_brochure
from .llm_clients.ollama_client import ollama_brochure
from .llm_clients.ovo_client import ovo_brochure


def get_brochure_user_prompt(subject: str, url: str, api: str, major: str) -> str:
    user_prompt = f"You are looking at a University Degree Program called: {subject}\n"
    user_prompt += (
        "Here are the contents of its landing page and other relevant pages; "
        "use this information to build a short brochure of the Degree Program in markdown.\n"
    )
    user_prompt += get_all_details(url, api)
    user_prompt = user_prompt[:5_000]  # Truncate if more than 5,000 characters
    return user_prompt

    user_prompt = f"You are looking at a University {major} Degree Program called: {subject}\n"
    user_prompt += (
        "Here are the contents of its landing page and other relevant pages; "
        "use this information to build a short brochure of the Degree Program in markdown.\n"
    )
    user_prompt += get_all_details(url, api)
    user_prompt = user_prompt[:5_000]



def create_brochure(subject: str, url: str, api: str, major: str) -> str:
    if api is None:
        api = input(
            "Which api would you like to use?\n"
            "A: OpenAI (GPT)\n"
            "B: Ollama (Llama 3.2)\n"
            "C: Ollama via OpenAI (Llama 3.2)\n"
            "D: Claude-haiku via anthropic\n"
        )

    user_prompt = get_brochure_user_prompt(subject, url, api, major)

    if (api.lower() == "a") or (api.lower() == "openai"):
        return openai_brochure(user_prompt, major)
    elif (api.lower() == "b") or (api.lower() == "ollama"):
        return ollama_brochure(user_prompt, major)
    elif (api.lower() == "c") or (api.lower() == "ollama via openai"):
        return ovo_brochure(user_prompt, major)
    elif (api.lower() == "d") or (api.lower() == "claude"):
        return claude_brochure(user_prompt, major)
    else:
        raise ValueError("Unknown API choice. Use A, B, C, or D.")


def stream_brochure(subject: str, url: str, api: str):
    """Stream brochure (OpenAI only), keeping signature similar to original intent."""
    user_prompt = get_brochure_user_prompt(subject, url, api)
    return openai_stream_brochure(user_prompt)
