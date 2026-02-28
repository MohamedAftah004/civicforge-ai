# 🏙️ CivicForge AI

AI Agent for Practical Software Solutions in Egypt

CivicForge AI is an agentic system designed to analyze real-world problems and propose realistic, implementable software solutions tailored specifically for Egypt.

The system generates structured solutions and then applies a feasibility guard to ensure practicality, affordability, and local suitability.

---

## 🎯 Purpose

Many real-world problems are solved with unrealistic or overly complex ideas.

CivicForge AI ensures that every proposed solution:

- Is software-based
- Is practical in Egypt
- Avoids expensive infrastructure
- Prefers mobile-first and low-cost approaches

---

## 🧠 How It Works

User Problem  
→ Solution Generator Agent  
→ Feasibility Guard Agent  
→ Final Practical Solution

---

## 🛡️ Feasibility Guard

After generating a draft solution, a second agent reviews it and:

- Removes unrealistic infrastructure
- Replaces expensive assumptions
- Adapts for small cities & municipalities
- Prioritizes mobile apps, SMS, and scalable tools
- Ensures cost-effectiveness

The final output is rewritten in clear Egyptian Arabic.

---

## ⚙️ Tech Stack

- Python
- FastAPI
- OpenAI-compatible LLM API
- Multi-Agent Architecture
- Structured Prompt Design

---


## 🚀 Running the Project

1. Install dependencies:

pip install -r requirements.txt

2. Run the API:
   uvicorn app.main:app --reload

3. Send a request:

POST `/analyze`

```json
{
  "problem": "Traffic congestion in small cities",
  "location": "Egypt"
}
```

`Output Structure`

The response always follows this format:
Problem Analysis
Proposed Software Solution
Core Features
Suggested Tech Stack
Implementation Steps
Expected Impact

---

`Key Characteristics`

Agent-based architecture

Structured output enforcement

Feasibility validation layer

Egypt-specific adaptation

Low-cost system design mindset
