import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from src.infra.database.models.base import BaseModel, TimestampMixin

from src.infra.dto.questions import QuestionDTO


class Question(BaseModel, TimestampMixin):
    id: Mapped[int] = mapped_column(sa.INT, primary_key=True)
    question: Mapped[str] = mapped_column(sa.VARCHAR)
    answer: Mapped[str] = mapped_column(sa.VARCHAR)

    def to_dto(self) -> QuestionDTO:
        return QuestionDTO(
            id=self.id,
            question=self.question,
            answer=self.answer,
            created_at=self.created_at,
            updated_at=self.updated_at
        )
