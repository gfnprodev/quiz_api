from typing import Literal, Type, Optional, TypeVar

import aiohttp
from aiohttp import ClientSession, ClientResponse

from src.common.utilities.api_requests.questions.handle_response import handle_response
from src.infra.schemas.base import BaseSchemaModel

T = TypeVar('T', bound=Optional[BaseSchemaModel])
class HttpClient:
    def __init__(self):
        self.base_url = "https://jservice.io/api/random"
        self.http_client: ClientSession | None = None

    async def get_http_client(self):
        if (not self.http_client) or self.http_client.closed:
            self.http_client = aiohttp.ClientSession()

        return self.http_client

    async def http_request(self, method: Literal['GET', 'POST'], params: dict) -> ClientResponse:
        session = await self.get_http_client()
        try:
            request = await session.request(method, self.base_url, params=params)
            return request
        except TimeoutError:
            raise TimeoutError

    async def request(self, method: Literal['GET', 'POST'], params: dict, response: Type[T] | Type[list[T]] = None) -> T | list[T]:
        request = await self.http_request(method, params)
        return await handle_response(request, response)

    async def close_session(self):
        await self.http_client.close()
