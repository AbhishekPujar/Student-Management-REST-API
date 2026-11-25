
# Student Management REST API

## Project Description
A Python REST API built using Flask and SQLite to manage student records.

## Technologies Used
- Python
- Flask
- SQLite
- SQL
- REST API
- API Key Authentication

## Features
- Add student records
- View all students
- View individual student
- Update student information
- Delete student records
- API key authentication
- Input validation
- Error handling
- Permanent database storage

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | / | API home |
| GET | /api/students | View all students |
| GET | /api/students/1 | View one student |
| POST | /api/students | Add student |
| PUT | /api/students/1 | Update student |
| DELETE | /api/students/1 | Delete student |

## Authentication
Use the X-API-Key request header.

Testing key: student123456

## How to Run

1. Create a virtual environment.
2. Install requirements.
3. Run python app.py.
4. Test endpoints using curl or Postman.

## Database
SQLite database stores student ID, name, course and email.

## Author
Student Project
