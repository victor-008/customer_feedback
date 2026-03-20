from pydantic import BaseModel

class FeedbackInput(BaseModel):
    text: str

    class FeedbackResult(BaseModel):
        category: str
        problem: str | None
        customer_solution:str | None
        solution_valid: str | None
        recommended_solution: str | None