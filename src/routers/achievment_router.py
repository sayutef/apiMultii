from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.models import models
from src.schemas import schemas
from src.controllers import achievment_controller
from src.db.database import get_db

router = APIRouter(
    prefix="/achievements",
    tags=["Achievements"]
)

@router.post("/", response_model=schemas.Achievement, status_code=201)
def create_achievement(
    achievement_data: schemas.AchievementCreate,
    db: Session = Depends(get_db)
):
    return achievment_controller.create_achievement(db, achievement_data)

@router.get("/", response_model=list[schemas.Achievement])
def get_all_achievements(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return achievment_controller.get_all_achievements(db, skip=skip, limit=limit)
