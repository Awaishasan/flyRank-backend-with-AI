from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.routes.task_routes import router as tasks_router
from app.data.database import init_db

from app.routes.auth_router import router as auth_router
from app.routes.public_router import router as public_router
from app.routes.protected_router import router as protected_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(
    title="Todo API",
    description="A simple SQLite Todo API with full CRUD operations.",
    version="1.0.0",
    lifespan=lifespan
)


app.include_router(tasks_router)
app.include_router(auth_router)
app.include_router(public_router)
app.include_router(protected_router)


@app.get("/")
def read_root():
    return {"message": "Hello, server!"}


@app.get("/health")
def read_health():
    return {"status": "ok"}