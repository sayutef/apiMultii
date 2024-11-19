from pydantic import BaseModel

class TeacherLogin(BaseModel):
    email: str
    password: str

class StudentLogin(BaseModel):
    registration_number: int
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str