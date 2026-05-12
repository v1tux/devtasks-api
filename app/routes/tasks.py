from fastapi import APIRouter
from app.schemas.task import TaskCreate

router = APIRouter()

tasks = []
task_id_counter = 1


@router.get("/tasks")
def list_tasks():
    return tasks


@router.post("/tasks")
def create_task(task: TaskCreate):
    global task_id_counter

    new_task = {
        "id": task_id_counter,
        "title": task.title,
        "done": False
    }

    tasks.append(new_task)

    task_id_counter += 1

    return {
        "message": "Task created successfully",
        "task": new_task
    }