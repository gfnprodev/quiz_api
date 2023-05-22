from typing import TYPE_CHECKING, Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.infra.database.dao.base import BaseDAO
from src.infra.database.models.questions import Question
from src.infra.schemas.question.create import CreateQuestionSchema

if TYPE_CHECKING:
    from src.infra.dto.questions import QuestionDTO


class QuestionDAO(BaseDAO):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session)

    async def add_questions(self, questions: list[CreateQuestionSchema]) -> int:
        question_ids = [question.id for question in questions]
        stmt = select(Question).where(Question.id.in_(question_ids))
        result = await self._session.scalars(stmt)

        exist_questions: Sequence[Question] = result.all()

        existing_question_ids = [question.id for question in exist_questions]
        new_question_ids = list(set(question_ids) - set(existing_question_ids))

        new_questions = []
        for question in questions:
            if question.id in new_question_ids:
                new_question = Question(id=question.id, question=question.question, answer=question.answer,
                                        created_at=question.created_at)
                new_questions.append(new_question)

        self._session.add_all(new_questions)
        return len(questions)-len(new_questions)

    async def get_last_question(self) -> "QuestionDTO":
        stmt = select(Question).order_by(Question.id.desc())

        result = await self._session.scalars(stmt)

        question: Question = result.first()

        return question.to_dto()
