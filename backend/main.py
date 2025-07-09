from contextlib import asynccontextmanager

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from backend.app.api.v1 import api_router
from backend.app.core.settings import settings
from backend.app.database import sessionmanager


@asynccontextmanager
async def lifespan(_app: FastAPI):
    yield

    if sessionmanager._engine is not None:
        await sessionmanager.close()


app = FastAPI(
    title="Store Management API",
    description="API для работы с Backend'ом магазина.",
    version="1.0.0",
    servers=[
        {"url": "http://localhost:8000", "description": "Local Development Server"}
    ],
    docs_url=None,
    redoc_url=None,
    lifespan=lifespan
)

cors_origins = settings.frontend_urls.split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Frontend origin
    # allow_origins=cors_origins,  # Frontend origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

app.include_router(api_router, prefix="/api")
