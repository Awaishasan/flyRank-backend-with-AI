from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.task import TaskResponse
from app.data.tasks import tasks

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.get("/", response_model=List[TaskResponse])
def get_tasks():
    return tasks

@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")
