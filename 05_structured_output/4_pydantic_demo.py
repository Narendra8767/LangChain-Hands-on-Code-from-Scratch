from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel):
    
    name:str
    age: Optional[int] = None
    email:EmailStr
    cgpa:float = Field(gt=0,lt=10,default=6,description="Performance of Stdent") # Add Constraint

new_student = {"name":"Nitish","age":21,"email":"abc@gmail.com","cgpa":5}

student = Student(**new_student)

print(student)
# student_json = student.model_dump_json()