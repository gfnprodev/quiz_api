from dataclasses import dataclass
from datetime import datetime


@dataclass
class QuestionDTO:
    id: int
    question: str
    answer: str
    created_at: datetime
    updated_at: datetime
