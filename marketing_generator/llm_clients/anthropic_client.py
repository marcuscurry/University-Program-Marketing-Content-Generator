from platform import system

from marketing_generator.config import CLAUDE_MODEL
from marketing_generator.prompts import system_prompt_student, system_prompt_links, system_prompt_brochure
from anthropic import Anthropic
import json
from IPython.display import Markdown, update_display, display
import re

def get_links_claude(system_prompt, user_message):
    client = Anthropic()
    claude = client.messages.create(
        model=CLAUDE_MODEL,
        max_tokens=1024,
        system=system_prompt,
        messages=user_message,
    )
    try:
        # Extract only the JSON part from Claude's response using a regex
        raw_text = claude.content[0].text
        match = re.search(r'\{.*\}', raw_text, re.DOTALL)
        if not match:
            raise ValueError("No valid JSON object found in Claude's response.")
        json_text = match.group(0)
        return json.loads(json_text)
    except Exception as e:
        print("Claude returned invalid JSON:", raw_text)
        raise e


def claude_brochure(user_prompt: str) -> str:
    client = Anthropic()
    claude = client.messages.create(
        model=CLAUDE_MODEL,
        max_tokens=1024,
        system=system_prompt_brochure,
        messages=[{'role':'user', 'content':user_prompt}]
    )
    return claude.content[0].text

def stream_claude_brochure(prompt: str):
    client = Anthropic()
    claude = client.messages.stream(
        model="claude-3-haiku-20240307",
        max_tokens=1000,
        temperature=0.7,
        system=system_prompt_brochure,
        messages=[
            {"role": "user", "content": prompt},
        ]
    )

    response = ""
    with claude as stream:
        for text in stream.text_stream:
            response += text or ""
            yield response