from pydantic import BaseModel
from typing import Optional

class TaskBase(BaseModel):
    title: str
    done: bool = False

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    done: Optional[bool] = None

class TaskResponse(TaskBase):
    id: int
