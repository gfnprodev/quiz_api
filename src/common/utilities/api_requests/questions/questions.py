from src.common.utilities.api_requests.questions.http_client import HttpClient

from src.infra.schemas.question.default import QuestionDefaultSchema


class QuestionsAPI(HttpClient):
    def __init__(self):
        super().__init__()

    async def get_questions(self, question_nums: int) -> list[QuestionDefaultSchema]:
        request = await self.request("GET", {"count": question_nums}, list[QuestionDefaultSchema])

        return request
