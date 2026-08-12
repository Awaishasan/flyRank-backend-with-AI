from fastapi import APIRouter, HTTPException, Response
from typing import List
from app.schemas.task import TaskResponse, TaskCreate, TaskUpdate
from app.data.tasks import tasks

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.get("/", response_model=List[TaskResponse], summary="Get all tasks")
def get_tasks():
    """Retrieve a list of all tasks."""
    return tasks

@router.get("/{task_id}", response_model=TaskResponse, summary="Get a specific task")
def get_task(task_id: int):
    """Retrieve a single task by its ID."""
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@router.post("/", response_model=TaskResponse, status_code=201, summary="Create a new task")
def create_task(task: TaskCreate):
    """Create a new task with a title and optional 'done' status."""
    if not task.title or not task.title.strip():
        raise HTTPException(status_code=400, detail="Title cannot be empty")
    new_id = len(tasks) + 1 if tasks else 1
    new_task = {"id": new_id, "title": task.title.strip(), "done": task.done}
    tasks.append(new_task)
    return new_task

@router.put("/{task_id}", response_model=TaskResponse, summary="Update an existing task")
def update_task(task_id: int, task_update: TaskUpdate):
    """Update a task's title, done status, or both."""
    for task in tasks:
        if task["id"] == task_id:
            if task_update.title is not None:
                if not task_update.title.strip():
                    raise HTTPException(status_code=400, detail="Title cannot be empty")
                task["title"] = task_update.title.strip()
            if task_update.done is not None:
                task["done"] = task_update.done
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@router.delete("/{task_id}", status_code=204, summary="Delete a task")
def delete_task(task_id: int):
    """Delete a task by its ID."""
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            del tasks[i]
            return Response(status_code=204)
    raise HTTPException(status_code=404, detail="Task not found")
