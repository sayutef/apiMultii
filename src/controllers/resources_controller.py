from sqlalchemy.orm import Session
from src.models import models
from src.schemas import schemas

def create_number(db: Session, video_data: schemas.VideoCreate):
    db_video = models.Numbers(**video_data.dict())
    db.add(db_video)
    db.commit()
    db.refresh(db_video)
    return db_video

def get_all_numbers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Numbers).offset(skip).limit(limit).all()

def create_write(db: Session, video_data: schemas.VideoCreate):
    db_video = models.WriteAndRead(**video_data.dict())
    db.add(db_video)
    db.commit()
    db.refresh(db_video)
    return db_video

def get_all_writes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.WriteAndRead).offset(skip).limit(limit).all()

def create_reading(db: Session, reading_data: schemas.Readings):
    db_reading = models.Readings(**reading_data.dict())
    db.add(db_reading)
    db.commit()
    db.refresh(db_reading)
    return db_reading

def get_all_readings(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Readings).offset(skip).limit(limit).all()
