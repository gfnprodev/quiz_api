from typing import Type, TypeVar, Optional

import pydantic
from aiohttp import ClientResponse

from src.infra.schemas.base import BaseSchemaModel

T = TypeVar('T', bound=BaseSchemaModel)


async def handle_response(response: ClientResponse, data_type: Optional[Type[T]] | Type[list[T]]) -> Optional[T] | Optional[list[T]]:
    if data_type is None:
        return None
    data = await response.json()
    response.close()
    return pydantic.parse_obj_as(data_type, data)
