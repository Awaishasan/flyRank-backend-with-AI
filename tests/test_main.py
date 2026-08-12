from fastapi.testclient import TestClient
import pytest
from app.main import app
from app.data.tasks import tasks

client = TestClient(app)

@pytest.fixture(autouse=True)
def clear_tasks():
    tasks.clear()
    yield

def test_hello_server():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, server!"}

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_get_tasks_empty():
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert response.json() == []

def test_get_task_not_found():
    response = client.get("/tasks/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Task not found"}

def test_create_task():
    response = client.post("/tasks/", json={"title": "New Task"})
    assert response.status_code == 201
    assert response.json() == {"id": 1, "title": "New Task", "done": False}

def test_create_task_empty_title():
    response = client.post("/tasks/", json={"title": "   "})
    assert response.status_code == 400
    assert response.json() == {"detail": "Title cannot be empty"}
