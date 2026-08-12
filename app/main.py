from fastapi import FastAPI

app = FastAPI(title="Todo API")

@app.get("/")
def read_root():
    return {"message": "Hello, server!"}
