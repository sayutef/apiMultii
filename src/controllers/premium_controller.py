from src.db.database import get_mongo_db
from src.schemas import schemas

premium_collection = get_mongo_db()["premium"]

# Crear Premium
async def create_premium(premium_data: schemas.PremiumCreate):
    try:
        # Verificar si student_id es un entero válido
        if not isinstance(premium_data.student_id, int):
            raise ValueError(f"Invalid student_id: {premium_data.student_id}")

        # Insertar en la colección "premium"
        premium = await premium_collection.insert_one({
            "student_id": premium_data.student_id,  # Now it's an integer
            "is_active": premium_data.is_active
        })

        # Devuelve el id del nuevo documento insertado
        return str(premium.inserted_id)  # Assuming you're using MongoDB's default ObjectId for the document

    except ValueError as ve:
        raise Exception(f"Error en la validación del ID: {ve}")
    except Exception as e:
        raise Exception(f"Error al crear el premium: {e}")

# Obtener Premium por estudiante
async def get_premium_by_student(student_id: int):
    premium = await premium_collection.find_one({"student_id": student_id})  # Search by integer student_id
    if premium:
        return schemas.Premium(**premium)  # Convertir a esquema Pydantic
    return None
