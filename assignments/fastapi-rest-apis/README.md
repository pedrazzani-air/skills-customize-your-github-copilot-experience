# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a basic REST API using FastAPI, including route creation, request validation, and proper HTTP responses.

## 📝 Tasks

### 🛠️ Create Your First API Endpoints

#### Description
Set up a FastAPI app and create foundational endpoints for a simple task manager API.

#### Requirements
Completed program should:

- Create a FastAPI app instance
- Add a `GET /` endpoint that returns a welcome message
- Add a `GET /tasks` endpoint that returns a list of tasks from in-memory data
- Run the API locally with Uvicorn


### 🛠️ Add Request Validation with Pydantic

#### Description
Use a Pydantic model to validate incoming data when creating new tasks.

#### Requirements
Completed program should:

- Define a `TaskCreate` model with fields: `title` (required), `completed` (default `False`)
- Add a `POST /tasks` endpoint that accepts and validates JSON input
- Return the created task with a generated `id`
- Reject invalid payloads automatically through FastAPI validation


### 🛠️ Implement Task Updates and Error Handling

#### Description
Add an endpoint to update task status and return meaningful errors when a task does not exist.

#### Requirements
Completed program should:

- Add a `PATCH /tasks/{task_id}` endpoint to update only the `completed` field
- Return a `404` error when `task_id` is not found
- Return the updated task as JSON
- Keep the code organized and easy to read
