from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from app.core.config import settings
from app.api.v1.health import router as health_router
from app.api.v1.auth import router as auth_router

app = FastAPI(title="InboxOS API")
app.add_middleware(
    SessionMiddleware,
    secret_key=settings.SESSION_SECRET,
    same_site="lax",
    https_only=False,  # set True in production
)

app.include_router(health_router)
app.include_router(auth_router)
app.get("/")
async def root():
    return {"message":"InboxOS API is running"}