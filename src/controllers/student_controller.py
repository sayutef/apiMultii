from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.models import models
from src.schemas import schemas

def delete_student_from_class(db: Session, student_id: int, class_id: int):
    db_student =db.query(models.Enrolled).filter(
        models.Enrolled.student_id == student_id,
        models.Enrolled.class_id == class_id
    )
    db.delete(db_student)
    db.commit()
    return db_student

def add_student_to_class(db: Session, enrollment_data: schemas.EnrolledCreate):
    existing_enrollment = db.query(models.Enrolled).filter(
        models.Enrolled.student_id == enrollment_data.student_id,
        models.Enrolled.class_id == enrollment_data.class_id
    ).first()
    
    if existing_enrollment:
        raise HTTPException(status_code=400, detail="Student is already enrolled in this class")

    enrollment = models.Enrolled(**enrollment_data.dict())
    db.add(enrollment)
    db.commit()
    db.refresh(enrollment)
    return enrollment

def get_students_by_class_id(db: Session, class_id: int, skip: int = 0, limit: int = 100):
    return (
        db.query(models.Student)
        .join(models.Enrolled, models.Student.id == models.Enrolled.student_id)
        .filter(models.Enrolled.class_id == class_id)
        .offset(skip)
        .limit(limit)
        .all()
    )