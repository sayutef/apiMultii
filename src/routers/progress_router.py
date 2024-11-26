from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from src.schemas.schemas import Progress  # Asegúrate de que el modelo 'Progress' esté bien importado desde tus esquemas
from bson import ObjectId
from pymongo import MongoClient  # Aquí estamos usando pymongo para conectar con MongoDB
from typing import List

# Configurar la conexión a la base de datos MongoDB (puedes configurar esto según tu entorno)
client = MongoClient("mongodb+srv://sayu:sayu123@letroapi.mgwg8.mongodb.net/")  # Cambia la URL si es necesario
db = client["letroapi"]  # Cambia 'your_database_name' por el nombre de tu base de datos
progress_collection = db["progress"]  # Colección de progresos en MongoDB

router_progress = APIRouter()


def format_progress(progress) -> dict:

    created_at = progress.get("createdAt")

    if created_at:
        if isinstance(created_at, datetime):
            created_at = created_at.strftime("%Y-%m-%d")
    else:
        created_at = "No date available"
    
    # Comprobar si existen los campos 'subject', 'progress' y 'student_id'
    subject = progress.get("subject", "No subject available")  # Valor por defecto si no existe
    progress_value = progress.get("progress", "No progress available")  # Valor por defecto si no existe
    student_id = progress.get("student_id", "No student ID available")  # Valor por defecto si no existe
    
    return {
        "id": str(progress["_id"]),  # Convertir el ObjectId a string
        "subject": subject,
        "progress": progress_value,
        "student_id": student_id,
        "createdAt": created_at
    }

@router_progress.get("/progress/all", response_model=List[dict])
def get_progresses():
    # Obtener todos los progresos desde la base de datos
    progresses = progress_collection.find()
    return [format_progress(progress) for progress in progresses]

@router_progress.post("/progress", status_code=201, response_model=dict)
def create_progress(progress: Progress):
    # Insertar un nuevo progreso en la base de datos
    new_progress = progress.dict(exclude={"id"})
    result = progress_collection.insert_one(new_progress)
    
    # Obtener el progreso recién creado
    created_progress = progress_collection.find_one({"_id": result.inserted_id})
    
    # Retornar el progreso formateado
    return format_progress(created_progress)

@router_progress.get("/progress/{progress_id}", response_model=dict)
def get_progress(progress_id: str):
    progress = progress_collection.find_one({"_id": ObjectId(progress_id)})
    if not progress:
        raise HTTPException(status_code=404, detail="Progress not found")
    return format_progress(progress)

@router_progress.delete("/delete/{progress_id}", response_model=dict)
def delete_progress(progress_id: str):
    result = progress_collection.delete_one({"_id": ObjectId(progress_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Progress not found")
    return {"message": "Progress deleted successfully"}
