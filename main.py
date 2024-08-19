# Import necessary modules from FastAPI, typing and pydantic
from fastapi import FastAPI, Path  # FastAPI for creating the app and Path for defining path parameters
from typing import Optional  # Optional allows defining optional query parameters
from pydantic import BaseModel  # BaseModel for defining request bodies

# This is to create an instance of the FastAPI class which will serve as the main app
app = FastAPI()

# Sample in-memory data representing students
students = {
    1: {
        "name": "john",
        "age": 17,
        "year": "year 12"
    }
}

# Define a Pydantic model for the student
# This is used for validating and parsing request bodies
class Student(BaseModel):
    name: str
    age: int
    year: str
    
# Define a Pydantic model for updating the student
class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None

# Define the root endpoint ("/") of the application
# When accessed it returns a simple JSON response
@app.get("/")
def index():
    return {"name": "First Data"}  # Root response with a dictionary containing a welcome message

# Define an endpoint to get a student's information by their ID
# student_id is passed as a path parameter which must be an integer greater than 0
@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(description="The ID of the student you want to view", gt=0)):
    return students.get(student_id, {"Error": "Student not found"})  # Return the student information or an error if not found

# Define an endpoint to get a student's information by their name and an additional test parameter
# name is passed as an optional query parameter test is a required query parameter
@app.get("/get-by-name")
def get_student(*, name: Optional[str] = None, test: int):
    for student_id, student in students.items(): # Iterate over all students in the dictionary to find a match by name
        if student["name"] == name:  # If a matching name is found
            return student  # Return the student's information
    
    # If no student is found with the provided name then return a "Data not found" message
    return {"Data": "Not found"}

# Define an endpoint that combines a path parameter (student_id) and query parameters (name and test)
# This allows fetching a student's information based on both ID and name
@app.get("/get-by-name/{student_id}")
def get_student(*, student_id: int, name: Optional[str] = None, test: int):
    if student_id in students and students[student_id]["name"] == name:  # Check if the student ID exists and the name matches
        return students[student_id]  # Return the student's information
    
    # If no match is found then return a "Data not found" message
    return {"Data": "Not found"}

# Define an endpoint to create a new student using a POST request
# The student_id is passed as a path parameter and the student data is passed as a request body
@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student already exists"}  # Return an error if the student ID already exists
    
    students[student_id] = student.dict()  # Add the new student to the dictionary
    return students[student_id]  # Return the newly created student's information

# Define an endpoint to update an existing student using a PUT request
# The student_id is passed as a path parameter and the update data is passed as a request body
@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "Student does not exist"}  # Return an error if the student ID doesn't exist

    # Update only the fields that are provided in the request body
    if student.name is not None:
        students[student_id]["name"] = student.name
    if student.age is not None:
        students[student_id]["age"] = student.age
    if student.year is not None:
        students[student_id]["year"] = student.year

    return students[student_id]  # Return the updated student's information

# Define an endpoint to delete a student using a DELETE request
@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error": "Student does not exist"}  # Return an error if the student ID doesn't exist
    
    del students[student_id]  # Delete the student from the dictionary
    return {"Message": "Student deleted successfully"}  # Return a success message
