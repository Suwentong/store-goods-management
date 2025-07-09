from fastapi import APIRouter

from .endpoints import authorization

api_router = APIRouter()

api_router.include_router(authorization.router, prefix="/authorization", tags=["Авторизация"])
