from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.models import models
from src.schemas import schemas
from src.controllers import submissions_controller
from src.db.database import get_db
from src.middlewares.auth_middleware import teacher_middleware, generic_middleware, student_middleware

router = APIRouter(
    prefix="/submissions",
    tags=["Submissions"]
)

@router.post("/", response_model=schemas.Submission, status_code=201, )
def create_submission(
    submission_data: schemas.SubmissionCreate,
    db: Session = Depends(get_db)
):
    return submissions_controller.create_submission(db, submission_data)

@router.get("/task/{task_id}", response_model=list[schemas.Submission])
def get_submissions_by_task(
    task_id: int,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return submissions_controller.get_submissions_by_task_id(db, task_id, skip=skip, limit=limit)
