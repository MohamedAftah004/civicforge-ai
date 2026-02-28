from openai import OpenAI
from app.config import LLM_MODEL

FEASIBILITY_PROMPT = """
You are a Feasibility Guard Agent.

Your job is to review a proposed software solution
for real-world problems in Egypt.

Rules:
- Remove or replace any solution that requires:
  * expensive hardware
  * advanced infrastructure
  * large-scale sensors or cameras
- Prefer:
  * mobile-first solutions
  * SMS or USSD fallbacks
  * low-cost and scalable tools
- Adapt solutions for small cities and municipalities
- Do NOT introduce new ideas unless needed for feasibility

Rewrite the solution to be realistic, low-cost,
and suitable for Egypt.

Return the FULL revised solution using the same structure By Arabic Egyptian accent.
"""

def run_feasibility_guard(client: OpenAI, draft_solution: str) -> str:
    response = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[
            {"role": "system", "content": FEASIBILITY_PROMPT},
            {"role": "user", "content": draft_solution}
        ],
        temperature=0.4
    )

    return response.choices[0].message.content