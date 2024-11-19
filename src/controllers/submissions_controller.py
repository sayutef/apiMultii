# controllers/submission_controller.py

from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.models import models
from src.schemas import schemas

def create_submission(db: Session, submission_data: schemas.SubmissionCreate):
    """
    Crea una nueva entrega de tarea (Submission) en la base de datos.
    """
    db_submission = models.Submission(**submission_data.dict())
    db.add(db_submission)
    db.commit()
    db.refresh(db_submission)
    return db_submission

def get_submissions_by_task_id(db: Session, task_id: int, skip: int = 0, limit: int = 100):
    """
    Obtiene todas las entregas de una tarea específica.
    """
    return (
        db.query(models.Submission)
        .filter(models.Submission.task_id == task_id)
        .offset(skip)
        .limit(limit)
        .all()
    )
