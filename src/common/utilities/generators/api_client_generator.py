from src.common.utilities.api_requests.questions.questions import QuestionsAPI


async def get_api_client_session() -> QuestionsAPI:
    api_client = QuestionsAPI()
    try:
        yield api_client
    finally:
        await api_client.close_session()
