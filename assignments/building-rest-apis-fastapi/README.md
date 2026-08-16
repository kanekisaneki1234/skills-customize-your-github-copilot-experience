# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a small REST API with FastAPI by creating endpoints for reading and creating data, using request validation, and returning JSON responses.

## 📝 Tasks

### 🛠️ Create a FastAPI App

#### Description
Set up a basic FastAPI application and confirm it runs locally with a simple health endpoint.

#### Requirements
Completed program should:

- Import `FastAPI` and create an app instance.
- Add a root or health endpoint that returns a JSON response.
- Start the app with Uvicorn or a similar ASGI server.
- Verify that the app responds successfully in a browser or with a request tool.

### 🛠️ Build a Resource API

#### Description
Create endpoints that let users view and create records for a simple resource such as books, students, or tasks.

#### Requirements
Completed program should:

- Define a data model for the resource using Python classes or Pydantic models.
- Add a `GET` endpoint to return all items.
- Add a `POST` endpoint to add a new item.
- Return JSON data in a clear, RESTful format.
- Include a unique identifier for each item.

### 🛠️ Add Validation and Error Handling

#### Description
Improve the API so it handles invalid input and missing resources gracefully.

#### Requirements
Completed program should:

- Validate incoming request data before creating new records.
- Return a useful error message when a requested item does not exist.
- Handle missing required fields with validation errors.
- Keep the API responses consistent and readable.

