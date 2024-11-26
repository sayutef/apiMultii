from bson import ObjectId
from src.db.database import get_mongo_db
from src.schemas import schemas

# MongoDB Collections
progress_collection = get_mongo_db()["progress"]

# Crear Progress
async def create_progress(progress_data: schemas.ProgressCreate):
    # Ensure you're passing progress_data and processing it correctly
    progress_document = {
        "subject": progress_data.subject,
        "progress": progress_data.progress,
        "student_id": progress_data.student_id,
    }
    
    result = await progress_collection.insert_one(progress_document)

    progress_document["id"] = str(result.inserted_id)  # Convert ObjectId to string
    return progress_document

# Obtener Progress por estudiante
async def get_progress_by_student(student_id: str):
    try:
        progress = await progress_collection.find_one({"student_id": student_id})  # Use string for student_id
        if progress:
            progress["id"] = str(progress["_id"])  # Convert ObjectId to string
            return schemas.Progress(**progress)
        return None
    except Exception as e:
        raise ValueError(f"Error retrieving progress: {e}")

# Actualizar Progress
async def update_progress(progress_id: str, progress_data: schemas.ProgressUpdate):
    try:
        result = await progress_collection.update_one(
            {"_id": ObjectId(progress_id)},  # Filter by MongoDB ID
            {"$set": {"counter_point": progress_data.counter_point}}  # Update counter_point
        )

        if result.modified_count == 0:
            return None

        updated_progress = await progress_collection.find_one({"_id": ObjectId(progress_id)})
        updated_progress["id"] = str(updated_progress["_id"])  # Convert ObjectId to string
        return schemas.Progress(**updated_progress)
    except Exception as e:
        raise ValueError(f"Error updating progress: {e}")
