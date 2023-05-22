from datetime import datetime

from src.infra.schemas.base import BaseSchemaModel


class CreateQuestionSchema(BaseSchemaModel):
    id: int
    question: str
    answer: str
    created_at: datetime
