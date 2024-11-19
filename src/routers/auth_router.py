from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from src.models import models
from src.schemas import auth_schemas, schemas
from src.controllers import auth_controller, register_controller
from src.db.database import get_db

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@router.post("/login/teachers", response_model=auth_schemas.Token)
def teacher_login(
    login_data: auth_schemas.TeacherLogin,
    db: Session = Depends(get_db)
):
    return auth_controller.teacher_login(db, login_data.email, login_data.password)

@router.post("/login/students", response_model=auth_schemas.Token)
def student_login(
    login_data: auth_schemas.StudentLogin,
    db: Session = Depends(get_db)
):
    return auth_controller.student_login(db, login_data.registration_number, login_data.password)

@router.post("/register/teachers", response_model=auth_schemas.Token, status_code=201)
def register_teacher(
    teacher_data: schemas.TeacherCreate,
    db: Session = Depends(get_db)
):
    return register_controller.teacher_register(db, teacher_data)

@router.post("/register/students", response_model=auth_schemas.Token, status_code=201)
def register_student(
    student_data: schemas.StudentCreate,
    db: Session = Depends(get_db)
):
    return register_controller.student_register(db, student_data)
