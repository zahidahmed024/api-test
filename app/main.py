from fastapi import FastAPI
from app.core.database import engine, Base
from app.modules.users.controller import router as user_router

app = FastAPI()

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(user_router, prefix="/users", tags=["Users"])
