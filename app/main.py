from fastapi import FastAPI
from app.routes.tasks import router as tasks_router

app = FastAPI(title="DevTasks API")


@app.get("/health")
def health_check():
    return {"status": "ok"}

app.include_router(tasks_router)

@app.get("/tasks")
def get_tasks():
    return tasks

@app.post("/tasks")
def create_task(task: dict):
    tasks.append(task)
    return {
        "message": "Task created successfully", 
        "task": task
        }
