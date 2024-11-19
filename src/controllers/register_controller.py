from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.models import models
from src.services.encrypt_service import hash_password
from src.schemas.auth_schemas import Token
from src.schemas.schemas import TeacherCreate, StudentCreate
from src.services.jwt_service import create_token

def teacher_register(db: Session, teacher_data: TeacherCreate) -> Token:
    if db.query(models.Teacher).filter(models.Teacher.email == teacher_data.email).first():
        raise HTTPException(status_code=400, detail="Correo ya existente")

    new_teacher = models.Teacher(
        name=teacher_data.name,
        email=teacher_data.email,
        password=hash_password(teacher_data.password)
    )
    db.add(new_teacher)
    db.commit()
    db.refresh(new_teacher)
    
    token = create_token({"teacher_id": new_teacher.id})
    return Token(access_token=token, token_type="bearer")

def student_register(db: Session, student_data: StudentCreate) -> Token:
    if db.query(models.Student).filter(
        models.Student.registration_number == student_data.registration_number
    ).first():
        raise HTTPException(status_code=400, detail="La matrícula ya existe")

    new_student = models.Student(
        name=student_data.name,
        paternal_surname=student_data.paternal_surname,
        maternal_surname=student_data.maternal_surname,
        registration_number=student_data.registration_number,
        password=hash_password(student_data.password)
    )
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    
    token = create_token({"student_id": new_student.id})
    return Token(access_token=token, token_type="bearer")