from fastapi import FastAPI
import uvicorn

app = FastAPI()


students : list = [
    {"id": 1, "name": "John", "age": 20, "grade": "A"},
    {"id": 2, "name": "Emily", "age": 19, "grade": "B"},
    {"id": 3, "name": "Michael", "age": 21, "grade": "C"},
    {"id": 4, "name": "Sarah", "age": 22, "grade": "A+"},
]

#Student Index
@app.get("/students")
def student_list():
    return students

# Show Student
@app.get("/students/{id}")
def get_student(id: int):
    student = {student["id"]: student for student in students}.get(id)
    if student is None:
        return {"message": "No Student exist with this id"}
    return student

# Add Student
@app.post("/students/")
def add_student(id: int, name: str, age: int, grade: str):
    students.append(
        {
            "id": id, 
            "name": name, 
            "age": age, 
            "grade": grade
            }
    )
    return  {"message" : "Student added successfully."}

# Update Student
@app.put("/students/{id}")
def update_student(id: int, name: str, age: int, grade: str):
    student = {student["id"]: student for student in students}.get(id)
    if student is None:
        return {"message": "No Student exist with this id"}
    student['name'] = name
    student['age'] = age
    student['grade'] = grade
    return student


# Delete Student
@app.delete("/students/{id}")
def remove_student(id: int):
    student = {student["id"]: student for student in students}.get(id)
    if student is None:
        return {"message": "No Student exist with this id"}
    students.remove(student)
    return  {"message" : "Student deleted successfully."}



def start():
    uvicorn.run('student.main:app', host='127.0.0.1', port=5000, reload=True)
