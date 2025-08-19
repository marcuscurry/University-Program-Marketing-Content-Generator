from .prompts import get_system_prompt_student
from .llm_clients.ollama_client import judge_brochures


def build_student_user_prompt(brochure_1: str, brochure_2: str, brochure_3: str, major: str) -> str:
    user_prompt_student = f"""
        You are a prospective {major} student comparing three programs based on their marketing materials. 
        Please **rank the underlying programs** — not the brochure formatting — using factors like:
        - Curriculum depth
        - Career opportunities
        - Alumni network
        - Global exposure
        - Uniqueness of the experience
        
        Give a ranked list and explain your reasoning.
        {brochure_1}
        {brochure_2}
        {brochure_3}
        
        Be sure to rank in Descending order (best to worst) and respond in Markdown.
        """
    return user_prompt_student



def rank_brochures(brochure_1: str, brochure_2: str, brochure_3: str, major: str) -> str:
    user_prompt_student = build_student_user_prompt(brochure_1, brochure_2, brochure_3, major)
    # Note: system_prompt_student is injected inside judge_brochures
    return judge_brochures(user_prompt_student, major)
