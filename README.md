## Description

Learning how to use FastAPI

## Project dependencies

`pip install fastapi`

`pip install uvicorn`

## How to test

1. To start server and automatically reload API changes: `uvicorn main:app --reload`

1. Send a request to `http://localhost:8000/` and receive `{"data:" "test"}`

1. Use `http://localhost:8000/docs` to see additional endpoints
