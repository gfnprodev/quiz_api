import logging

import fastapi
from fastapi import Depends

from src.common.misc.stub import Stub
from src.common.utilities.generators.api_client_generator import get_api_client_session
from src.infra.database.dao.holder import HolderDAO
from src.infra.schemas.question.default import QuestionDefaultSchema
from src.infra.schemas.question.get import QuestionNumSchema
from src.common.utilities.api_requests.questions.questions import QuestionsAPI

router = fastapi.APIRouter(prefix='/questions', tags=["Questions"])
logger = logging.getLogger(__name__)


@router.post(path="/",
             name="Add new questions",
             response_model=QuestionDefaultSchema,
             status_code=fastapi.status.HTTP_200_OK)
async def add_new_questions(questions_num: QuestionNumSchema, holder: HolderDAO = Depends(Stub(HolderDAO)),
                            questions_api: "QuestionsAPI" = Depends(get_api_client_session)):
    questions = await questions_api.get_questions(questions_num.questions_num)
    db_questions = await holder.question.add_questions(questions)

    while db_questions != 0:
        questions = await questions_api.get_questions(db_questions)
        db_questions = await holder.question.add_questions(questions)

    result_question = await holder.question.get_last_question()

    return QuestionDefaultSchema.from_orm(result_question)
