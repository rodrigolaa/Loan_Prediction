from pydantic import BaseModel
from typing import Optional, List

class Predictor(BaseModel):
    TotalIncome: int
    LoanAmount: int
    Credit_History: int
    Property_Area: int