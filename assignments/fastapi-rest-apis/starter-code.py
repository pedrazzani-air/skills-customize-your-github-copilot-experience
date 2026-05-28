"""Starter code for Building REST APIs with FastAPI assignment.

Run locally:
    uvicorn starter-code:app --reload
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Task Manager API")

# In-memory data store for the assignment.
tasks = [
    {"id": 1, "title": "Finish FastAPI homework", "completed": False},
    {"id": 2, "title": "Review API responses", "completed": True},
]


class TaskCreate(BaseModel):
    title: str
    completed: bool = False


class TaskStatusUpdate(BaseModel):
    completed: bool


@app.get("/")
def read_root():
    # TODO: Customize this message.
    return {"message": "Welcome to your FastAPI Task Manager!"}


@app.get("/tasks")
def list_tasks():
    # TODO: Return the list of tasks.
    return tasks


@app.post("/tasks")
def create_task(payload: TaskCreate):
    # TODO: Add input checks (for example, avoid empty titles).
    new_id = max(task["id"] for task in tasks) + 1 if tasks else 1
    task = {
        "id": new_id,
        "title": payload.title,
        "completed": payload.completed,
    }
    tasks.append(task)
    return task


@app.patch("/tasks/{task_id}")
def update_task_status(task_id: int, payload: TaskStatusUpdate):
    # TODO: Update only the completed status for the selected task.
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = payload.completed
            return task

    raise HTTPException(status_code=404, detail="Task not found")
