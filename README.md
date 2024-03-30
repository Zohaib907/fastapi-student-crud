# Student CRUD Application using FASTAPI

This is a simple CRUD (Create, Read, Update, Delete) application built with the FASTAPI framework. It allows you to manage student records.

## Features

- **Create**: Add new student.
- **Read**: Retrieve student information.
- **Update**: Modify existing student records.
- **Delete**: Remove student.

## Requirements

- Python 3.1.2
- Poetry
- FastAPI

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/Zohaib907/fastapi-student-crud.git
    ```


2. Install dependencies using Poetry:

    ```bash
    poetry install
    ```

## Usage

1. Start the application:

    ```bash
    poetry run dev
    ```

2. Once the server is running, navigate to `http://localhost:5000/docs` in your web browser to access the interactive API documentation (provided by Swagger UI). Here, you can test the API endpoints.

## API Endpoints

- **GET** `/students/`: Retrieve a list of all students.
- **GET** `/students/{student_id}`: Retrieve details of a specific student.
- **POST** `/students/`: Add a new student.
- **PUT** `/students/{student_id}`: Update details of a specific student.
- **DELETE** `/students/{student_id}`: Delete a student from the database.


