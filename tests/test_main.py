from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

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
