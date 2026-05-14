from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse
from app.services import task_service

router = APIRouter()


@router.get("/tasks", response_model=list[TaskResponse])
def list_task(
    done: bool | None = None,
    db: Session = Depends(get_db)
):
    return task_service.list_tasks(db, done)


@router.post(
    "/tasks",
    response_model=TaskResponse,
    status_code=201
)
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db)
):
    return task_service.create_task(db, task)

@router.put("/tasks/{task_id}")
def update_task(
    task_id: int,
    updated_task: TaskUpdate,
    db: Session = Depends(get_db)
):
    task = task_service.get_task_by_id(db, task_id)

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task_service.update_task(
        db,
        task,
        updated_task
    )

@router.delete("/tasks/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db)
):
    task = task_service.get_task_by_id(db, task_id)

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    task_service.delete_task(db, task)

    return {
        "message": "Task deleted successfully"
    }