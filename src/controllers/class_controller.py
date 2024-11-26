from sqlalchemy.orm import Session
from src.models import models
from src.schemas import schemas

def create_class(db: Session, classi: schemas.ClassCreate, teacher_id: int):
    # Crear la clase asignando explícitamente el teacher_id
    db_class = models.Class(
        id=classi.id,
        name=classi.name,
        description=classi.description,
        teacher_id=teacher_id  # Se asigna automáticamente al profesor autenticado
    )
    db.add(db_class)
    db.commit()
    db.refresh(db_class)
    return db_class

def get_classes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Class).offset(skip).limit(limit).all()

def get_class_by_professor_id(db: Session, professor_id: int):
    return (
        db.query(models.Class)
        .filter(models.Class.teacher_id == professor_id)
        .first()
    )
