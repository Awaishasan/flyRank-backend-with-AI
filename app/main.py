from fastapi import FastAPI
from app.routes.tasks import router as tasks_router

app = FastAPI(title="Todo API")
app.include_router(tasks_router)

@app.get("/")
def read_root():
    return {"message": "Hello, server!"}

@app.get("/health")
def read_health():
    return {"status": "ok"}
