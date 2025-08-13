import os
import dotenv

import openai
import requests  # noqa: F401 (imported for completeness; used by scraping)
from bs4 import BeautifulSoup  # noqa: F401
from IPython.display import Markdown, display, update_display  # noqa: F401
import ollama  # noqa: F401

# ==== CONSTANTS ====
OLLAMA_API = "http://localhost:11434/api/chat"
OLLAMA_MODEL = "llama3.2"
OPENAI_MODEL = "gpt-4o-mini"

# ==== REQUESTS HEADERS FOR SCRAPING ====
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/117.0.0.0 Safari/537.36"
    )
}

# ==== ENV ====
dotenv.load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY")
if openai.api_key:
    print("OpenAI API KEY FOUND")
else:
    print("OpenAI API KEY NOT FOUND")
