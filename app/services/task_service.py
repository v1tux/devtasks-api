from sqlalchemy.orm import Session

from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate


def list_tasks(db: Session, done: bool | None = None):
    query = db.query(Task)

    if done is not None:
        query = query.filter(Task.done == done)

    return query.all()


def get_task_by_id(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()


def create_task(db: Session, task: TaskCreate):
    new_task = Task(
        title=task.title
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task


def update_task(db: Session, task: Task, task_data: TaskUpdate):
    task.title = task_data.title
    task.done = task_data.done

    db.commit()
    db.refresh(task)

    return task


def delete_task(db: Session, task: Task):
    db.delete(task)
    db.commit()