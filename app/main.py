from fastapi import FastAPI

from app.routes.tasks import router as tasks_router
from app.database.base import Base
from app.database.connection import engine


app = FastAPI(title="DevTasks API")

Base.metadata.create_all(bind=engine)


@app.get("/health")
def health_check():
    return {"status": "ok"}

app.include_router(tasks_router)