from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session

from src.models import models
from src.schemas import schemas
from src.controllers import class_controller
from src.db.database import get_db
from src.middlewares.auth_middleware import teacher_middleware, student_middleware

router = APIRouter(
    prefix="/classes",
    tags=["Classes"]
)

@router.post("/", response_model=schemas.Class, status_code=201, dependencies=[Depends(teacher_middleware)])
def create_class(request: Request, classi: schemas.ClassCreate, db: Session = Depends(get_db)):
    teacher = request.state.teacher  # El profesor autenticado
    return class_controller.create_class(db, classi, teacher_id=teacher.id)

@router.get("/", response_model=list[schemas.Class], dependencies=[Depends(student_middleware)])
def get_classes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return class_controller.get_classes(db, skip=skip, limit=limit)

@router.get("/professor", response_model=schemas.Class, dependencies=[Depends(teacher_middleware)])
def get_class_by_professor(request: Request, db: Session = Depends(get_db)):
    teacher = request.state.teacher
    class_data = class_controller.get_class_by_professor_id(db, professor_id=teacher.id)
    if not class_data:
        raise HTTPException(status_code=404, detail="Class not found for the specified professor")
    return class_data