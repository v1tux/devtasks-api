from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate

router = APIRouter()


@router.get("/tasks")
def list_tasks(db: Session = Depends(get_db)):
    tasks = db.query(Task).all()

    return [
        {
            "id": task.id,
            "title": task.title,
            "done": task.done
        }
        for task in tasks
    ]


@router.get("/tasks/{task_id}")
def get_task(
    task_id: int,
    db: Session = Depends(get_db)
):
    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return {
        "id": task.id,
        "title": task.title,
        "done": task.done
    }


@router.post("/tasks")
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db)
):
    new_task = Task(
        title=task.title
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return {
        "message": "Task created successfully",
        "task": {
            "id": new_task.id,
            "title": new_task.title,
            "done": new_task.done
        }
    }


@router.put("/tasks/{task_id}")
def update_task(
    task_id: int,
    updated_task: TaskUpdate,
    db: Session = Depends(get_db)
):
    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    task.title = updated_task.title
    task.done = updated_task.done

    db.commit()
    db.refresh(task)

    return {
        "message": "Task updated successfully",
        "task": {
            "id": task.id,
            "title": task.title,
            "done": task.done
        }
    }

@router.delete("/tasks/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db)
):
    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    db.delete(task)
    db.commit()

    return {
        "message": "Task deleted successfully"
    }