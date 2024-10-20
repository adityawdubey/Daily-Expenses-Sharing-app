from pydantic import BaseModel
from typing import List, Optional

class ExpenseCreate(BaseModel):
    amount: float
    split_method: str
    user_id: int

class Expense(ExpenseCreate):
    id: int

    class Config:
        orm_mode = True

