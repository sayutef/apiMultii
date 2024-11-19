from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.models import models
from src.schemas import schemas
from src.services.jwt_service import create_token
from src.services.encrypt_service import verify_password

def teacher_login(db: Session, email: str, password: str):
    teacher = db.query(models.Teacher).filter(models.Teacher.email == email).first()
    if not teacher or not verify_password(password, teacher.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_token({"teacher_id": teacher.id})
    return {"access_token": token, "token_type": "bearer"}

def student_login(db: Session, registration_number: int, password: str):
    student = db.query(models.Student).filter(
        models.Student.registration_number == registration_number
    ).first()
    if not student or not verify_password(password, student.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_token({"student_id": student.id})
    return {"access_token": token, "token_type": "bearer"}