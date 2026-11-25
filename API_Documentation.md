
# Student Management REST API Documentation

## 1. Project Overview

The Student Management REST API is a Python-based application used to manage student records.

It allows users to add, view, update, and delete student information.

## 2. Technologies Used

- Python
- Flask
- SQLite
- REST API
- Pytest

## 3. Base URL

http://127.0.0.1:5000

## 4. Authentication

The API uses API Key authentication.

Add this header to protected requests:

X-API-Key: student123456

## 5. API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | / | Check API status |
| GET | /api/students | Get all students |
| GET | /api/students/1 | Get student by ID |
| POST | /api/students | Add a student |
| PUT | /api/students/1 | Update a student |
| DELETE | /api/students/1 | Delete a student |

## 6. Student Data Format

Example JSON:

{
    "name": "Abhishek",
    "course": "BCA",
    "email": "abhishek@example.com"
}

## 7. Response Status Codes

- 200: Successful request
- 201: Student created successfully
- 400: Invalid input
- 401: Unauthorized
- 404: Student not found
- 409: Email already exists

## 8. How to Run the Project

1. Activate the virtual environment.
2. Install dependencies.
3. Run the application using:

python app.py

4. Open the base URL in a browser.

## 9. Testing

Run the tests using:

python -m pytest -v
