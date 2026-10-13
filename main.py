from fastapi import FastAPI
from typing import Optional 
from pydantic import BaseModel

app = FastAPI() 

@app.get("/")
def read_root():
    return {"message": "Hello Sami"}

@app.get("/greet")
@app.get("/greet/{name}")
def greet(name: str = "Sam", age: Optional[int] = None, greeting: str = "Hello"):
    return {"message": f"{greeting} {name}", "age": age}

class Student(BaseModel):
    name: str
    age: int
    email: Optional[str] = None

@app.post("/create_student")
def create_student(student: Student):
    return {

        "name":student.name,
        "age":student.age,
        "email":student.email
    }

