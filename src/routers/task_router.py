from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.models import models
from src.schemas import schemas
from src.controllers import task_controller
from src.db.database import get_db
from src.middlewares.auth_middleware import teacher_middleware

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
    dependencies=[Depends(teacher_middleware)]
)

@router.get("/", response_model=list[schemas.Task])
def get_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return task_controller.get_tasks(db, skip=skip, limit=limit)

@router.get("/classes/{class_id}", response_model=list[schemas.Task])
def get_tasks_by_class_id(class_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return task_controller.get_tasks_by_class_id(db, class_id, skip=skip, limit=limit)

@router.post("/", response_model=schemas.Task, status_code=201)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return task_controller.create_task(db, task)

@router.put("/{task_id}", response_model=schemas.Task)
def update_task(task_id: int, task: schemas.TaskCreate, db: Session = Depends(get_db)):
    db_task = task_controller.update_task(db, task_id, task)
    if not db_task:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return db_task

@router.delete("/{task_id}", response_model=schemas.Task)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_task = task_controller.delete_task(db, task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return db_task