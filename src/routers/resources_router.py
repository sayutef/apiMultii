from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.models import models
from src.schemas import schemas
from src.controllers import resources_controller
from src.db.database import get_db

router = APIRouter(
    prefix="/resources",
    tags=["Resources"]
)

@router.post("/numbers", response_model=schemas.Video, status_code=201)
def create_number(
    achievement_data: schemas.VideoCreate,
    db: Session = Depends(get_db)
):
    return resources_controller.create_number(db, achievement_data)

@router.get("/numbers", response_model=list[schemas.Video])
def get_all_numbers(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return resources_controller.get_all_numbers(db, skip=skip, limit=limit)


@router.post("/writes", response_model=schemas.Video, status_code=201)
def create_write(
    achievement_data: schemas.VideoCreate,
    db: Session = Depends(get_db)
):
    return resources_controller.create_write(db, achievement_data)

@router.get("/writes", response_model=list[schemas.Video])
def get_all_writes(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return resources_controller.get_all_writes(db, skip=skip, limit=limit)

@router.post("/readings", response_model=schemas.Readings, status_code=201)
def create_number(
    achievement_data: schemas.ReadingsCreate,
    db: Session = Depends(get_db)
):
    return resources_controller.create_reading(db, achievement_data)

@router.get("/readings", response_model=list[schemas.Readings])
def get_all_numbers(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return resources_controller.get_all_readings(db, skip=skip, limit=limit)