from .prompts import system_prompt_student
from .llm_clients.ollama_client import judge_brochures


def build_student_user_prompt(ut_brochure: str, uc_brochure: str, uw_brochure: str) -> str:
    return (
        "Here are the three brochures you will be judging:\n\n"
        f"1. University of Texas {ut_brochure}\n"
        f"2. University of Chicago {uc_brochure}\n"
        f"3. University of Washington {uw_brochure}\n"
    )


def rank_brochures(ut_brochure: str, uc_brochure: str, uw_brochure: str) -> str:
    user_prompt_student = build_student_user_prompt(ut_brochure, uc_brochure, uw_brochure)
    # Note: system_prompt_student is injected inside judge_brochures
    return judge_brochures(user_prompt_student)
