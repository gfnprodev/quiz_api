from datetime import datetime

from pydantic import Field

from src.infra.schemas.base import BaseSchemaModel


class QuestionDefaultSchema(BaseSchemaModel):
    id: int
    question: str
    answer: str
    created_at: datetime


class QuestionListSchema(BaseSchemaModel):
    __root__: list[QuestionDefaultSchema] = Field(alias="questions")
