from sqlalchemy.ext.asyncio import AsyncSession

from src.infra.database.dao.base import BaseDAO
from src.infra.database.dao.question import QuestionDAO


class HolderDAO(BaseDAO):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session)
        self.question = QuestionDAO(session)
