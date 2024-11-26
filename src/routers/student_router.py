from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session

from src.models import models
from src.schemas import schemas
from src.controllers import student_controller
from src.db.database import get_db
from src.middlewares.auth_middleware import teacher_middleware, student_middleware

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)

@router.post("/classes", response_model=schemas.Enrolled)
def add_student_to_class(
    enrollment_data: schemas.EnrolledCreate,
    db: Session = Depends(get_db)
):
    return student_controller.add_student_to_class(db, enrollment_data)

@router.delete("/classes", response_model=schemas.Enrolled, dependencies=[Depends(teacher_middleware)])
def delete_student_from_class(
    student_id: int,
    class_id: int,
    db: Session = Depends(get_db)
):
    enrollment = student_controller.delete_student_from_class(db, student_id, class_id)
    if not enrollment:
        raise HTTPException(status_code=404, detail="Enrollment not found for the specified student and class")
    return enrollment

@router.get("/classes/{class_id}", response_model=list[schemas.Student], dependencies=[Depends(teacher_middleware)])
def get_students_by_class_id(
    class_id: int,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    students = student_controller.get_students_by_class_id(db, class_id, skip=skip, limit=limit)
    if not students:
        raise HTTPException(status_code=404, detail="No students found for the specified class")
    return students
