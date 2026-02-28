from pydantic import BaseModel


class ProblemRequest(BaseModel):
    problem: str
    location: str = "Egypt"