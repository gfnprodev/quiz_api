from fastapi import APIRouter

from src.routes.questions import questions


def register(root_router: APIRouter) -> None:
    for route in (
        questions,
    ):
        root_router.include_router(route.router)
