schemas.py
from pydantic import BaseModel

class UserInput(BaseModel):
    risk: int
    amount: float
    goal: str
