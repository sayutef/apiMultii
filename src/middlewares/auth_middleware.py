from fastapi import HTTPException, Depends, Request
from sqlalchemy.orm import Session
from src.db.database import get_db
from src.models.models import Teacher, Student
from src.services.jwt_service import verify_token

async def teacher_middleware(
    request: Request,
    token: dict = Depends(verify_token),
    db: Session = Depends(get_db)
):
    if "teacher_id" not in token:
        raise HTTPException(status_code=401, detail="Token de profesor inválido")
    
    teacher = db.query(Teacher).filter(Teacher.id == token["teacher_id"]).first()
    if not teacher:
        raise HTTPException(status_code=401, detail="Profesor no encontrado")
    
    request.state.teacher = teacher
    return teacher

async def student_middleware(
    request: Request,
    token: dict = Depends(verify_token),
    db: Session = Depends(get_db)
):
    if "student_id" not in token:
        raise HTTPException(status_code=401, detail="Token de estudiante inválido")
    
    student = db.query(Student).filter(Student.id == token["student_id"]).first()
    if not student:
        raise HTTPException(status_code=401, detail="Estudiante no encontrado")
    
    request.state.student = student
    return student

async def generic_middleware(
    request: Request,
    token: dict = Depends(verify_token),
    db: Session = Depends(get_db),
):
    
    if not ("student_id" in token or "teacher_id" in token):
        raise HTTPException(status_code=401, detail="Token inválido")
    
    student = db.query(Student).filter(Student.id == token.get("student_id")).first() if "student_id" in token else None
        
    teacher = db.query(Teacher).filter(Teacher.id == token.get("teacher_id")).first() if "teacher_id" in token else None

    if not student and not teacher:
        raise HTTPException(status_code=401, detail="Usuario no encontrado")
    
    if student:
        request.state.student = student
        return student
    else:
        request.state.teacher = teacher
        return teacher
