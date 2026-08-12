# FastAPI CRUD API
A simple in-memory Todo API built with FastAPI.

## Requirements
- Python 3.9+
- FastAPI
- Uvicorn
- Pytest

## Setup
1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment
4. Install dependencies: `pip install -r requirements.txt`

## Running the API
Run the server using uvicorn:
```bash
uvicorn app.main:app --reload
```
The API will be available at `http://127.0.0.1:8000`.

## API Documentation (Swagger UI)
Interactive API documentation is available at `http://127.0.0.1:8000/docs`.

![Swagger UI](swagger.png)

## Testing
Run the tests using pytest:
```bash
pytest tests
```

