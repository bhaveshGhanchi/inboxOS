from fastapi import FastAPI
from app.api.v1.health import router as health_router

app = FastAPI(title="InboxOS API")
app.include_router(health_router)

app.get("/")
async def root():
    return {"message":"InboxOS API is running"}