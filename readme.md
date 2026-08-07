# University Management System API

A REST API built with FastAPI and PostgreSQL for managing university data.

## Features
- JWT Authentication
- Role Based Access Control (Teacher/Student)
- Course Registration
- Student Management
- File Upload (Profile Pictures)
- Pagination + Search
- Alembic Database Migrations

## Tech Stack
- Python
- FastAPI
- PostgreSQL
- SQLAlchemy + Alembic
- Docker

## How to Run

### Local
1. Clone the repo
2. Create virtual environment
   python -m venv venv
   source venv/bin/activate
3. Install dependencies
   pip install -r requirements.txt
4. Create .env file
   database=postgresql://user:password@localhost:5432/dbname
5. Run migrations
   alembic upgrade head
6. Start server
   uvicorn main:app --reload
7. Open http://localhost:8000/docs

## API Endpoints

### Auth
POST /login           → get JWT token

### Courses (Teacher only)
POST /register_the_course  → register new course
GET  /all_class            → get all courses

### Students
GET  /get_student_data     → get student by id
POST /post_new_student     → add new student
PUT  /change_student_data  → update student

### Files
POST /uploadfile      → upload profile picture

### Search
GET  /pagination      → search + paginate students