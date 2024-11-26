from fastapi import APIRouter, HTTPException
from src.schemas import schemas
from src.controllers import premium_controller

router = APIRouter()

# Crear Premium
@router.post("/premium", response_model=schemas.Premium)
async def create_premium(premium_data: schemas.PremiumCreate):
    try:
        # Verificar si student_id es un entero válido
        if not isinstance(premium_data.student_id, int):
            raise ValueError(f"Invalid student_id: {premium_data.student_id}")
        
        premium_id = premium_data.student_id  # Use student_id as is, assuming integer ID
        premium = schemas.Premium(
            id=premium_id,
            student_id=premium_data.student_id,
            is_active=premium_data.is_active
        )

        # Simulamos guardar en la base de datos (MongoDB)
        # Aquí iría la lógica de guardado en la base de datos, por ejemplo:
        # db.save(premium)

        return premium

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error") from e

# Obtener Premium por estudiante
@router.get("/premium/{student_id}", response_model=schemas.Premium)
async def get_premium_by_student(student_id: int):  # Now student_id is an integer
    try:
        premium = await premium_controller.get_premium_by_student(student_id)
        if premium:
            return premium
        raise HTTPException(status_code=404, detail="Premium not found")
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error") from e
