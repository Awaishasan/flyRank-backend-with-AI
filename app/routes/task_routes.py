from fastapi import APIRouter, HTTPException, Response, Depends
from typing import List
from app.schemas.task_schema import TaskResponse, TaskCreate, TaskUpdate
from app.data.tasks import tasks
from app.data.database import get_db_connection

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.get("/", response_model=List[TaskResponse], summary="Get all tasks")
def get_tasks():
    """Retrieve a list of all tasks."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

@router.get("/{task_id}", response_model=TaskResponse, summary="Get a specific task")
def get_task(task_id: int):
    """Retrieve a single task by its ID."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return dict(row)
    raise HTTPException(status_code=404, detail="Task not found")

@router.post("/", response_model=TaskResponse, status_code=201, summary="Create a new task")
def create_task(task: TaskCreate):
    """Create a new task with a title and optional 'done' status."""
    if not task.title or not task.title.strip():
        raise HTTPException(status_code=400, detail="Title cannot be empty")
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO tasks (title, done) VALUES (?, ?)',
        (task.title.strip(), task.done)
    )
    conn.commit()
    new_id = cursor.lastrowid
    
    cursor.execute('SELECT * FROM tasks WHERE id = ?', (new_id,))
    row = cursor.fetchone()
    conn.close()
    
    return dict(row)

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
