# Prompts centralization

# Link selection system prompt (expects JSON of selected links)
system_prompt_links = (
    "You are provided with a list of links found on a University Program webpage. "
    "You are able to decide which of the links would be most relevant to include "
    "in a brochure/marketing summary about the program, such as links to an About page, "
    "or a University page, or Curriculum/Coursework pages.\n"
    "Do NOT invent or hallucinate links.\n"
    "You should respond in JSON as in this example:\n"
    '{\n'
    '    "links": [\n'
    '        {"type": "Curriculum page", "url": "https://full.url/goes/here/curriculum"},\n'
    '        {"type": "About page", "url": "https://another.full.url/"}\n'
    '    ]\n'
    '}\n'
)

# Brochure/Marketing generation system prompt
def get_system_prompt_brochure(major: str):
    system_prompt_brochure = (
        "You are an assistant that analyzes the contents of several relevant pages from a "
        "University Degree Program website and creates a short brochure/marketing summary "
        f"about the Program for prospective {major} students, partnerships and companies. "
        "Respond in markdown. Include details of University culture, academic benefits and "
        "prospective careers/jobs if you have the information. Lastly, be sure to tailor the "
        "information to prosepective students in that field and what they may prioritize."
    )
    return system_prompt_brochure

# Evaluation system prompt (student ranking the brochures)
def get_system_prompt_student(major: str):
    system_prompt_student = (
        f"You are a prospective {major} Master's student looking for the best program "
        f"to expand and launch your career into the {major} field. You will be presented with "
        f"three marketing brochures from University {major} Programs (in Markdown). "
        f"You will analyze them, and rank them from worst to best judging on any factors "
        f"you deem important and/or necessary. Respond in Markdown."
    )
    return system_prompt_student
