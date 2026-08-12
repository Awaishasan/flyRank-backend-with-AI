from fastapi import FastAPI
from app.routes.tasks import router as tasks_router

app = FastAPI(
    title="Todo API",
    description="A simple in-memory Todo API with full CRUD operations.",
    version="1.0.0"
)
app.include_router(tasks_router)

@app.get("/")
def read_root():
    return {"message": "Hello, server!"}

@app.get("/health")
def read_health():
    return {"status": "ok"}
