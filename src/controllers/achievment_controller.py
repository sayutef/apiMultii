from sqlalchemy.orm import Session
from src.models import models
from src.schemas import schemas

def create_achievement(db: Session, achievement_data: schemas.AchievementCreate):
    db_achievement = models.Achievement(**achievement_data.dict())
    db.add(db_achievement)
    db.commit()
    db.refresh(db_achievement)
    return db_achievement

def get_all_achievements(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Achievement).offset(skip).limit(limit).all()
