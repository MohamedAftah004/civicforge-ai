from fastapi import FastAPI
from openai import OpenAI
from app.schemas import ProblemRequest
from app.config import LLM_BASE_URL, LLM_MODEL, LLM_API_KEY
from app.agents.feasibility_guard import run_feasibility_guard

app = FastAPI(title="CivicForge AI")

@app.get("/")
def root():
    return {"status": "CivicForge AI is running"}

client = OpenAI(
    base_url=LLM_BASE_URL,
    api_key=LLM_API_KEY
)

SYSTEM_PROMPT = """
You are CivicForge AI, an expert agent specialized in proposing
practical software solutions for real-world problems in Egypt.

Rules:
- Only propose software-based solutions
- Solutions must be realistic and implementable in Egypt
- Avoid advanced or unrealistic infrastructure assumptions

Your response MUST follow this structure:

1. Problem Analysis
2. Proposed Software Solution
3. Core Features
4. Suggested Tech Stack
5. Implementation Steps
6. Expected Impact

If the problem is unclear or non-software-related, politely refuse.
"""

@app.post("/analyze")
def analyze_problem(req: ProblemRequest):
    initial_response = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": f"Problem: {req.problem}\nLocation: {req.location}"
            }
        ],
        temperature=0.6
    )

    draft_solution = initial_response.choices[0].message.content

    final_solution = run_feasibility_guard(client, draft_solution)

    return {
        "result": final_solution
    }

# @app.post("/analyze")
# def analyze_problem(req: ProblemRequest):
#     response = client.chat.completions.create(
#         model=LLM_MODEL,
#         messages=[
#         {
#             "role": "system", "content": SYSTEM_PROMPT},
#         {
#             "role": "user",
#             "content": f"Problem: {req.problem}\nLocation: {req.location}"
#         }],        
#         temperature=0.6
#     )

#     return {
#         "result": response.choices[0].message.content
#     }