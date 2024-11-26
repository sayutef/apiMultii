from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from src.models import models
from src.db.database import engine
from src.routers.student_router import router as student_router
from src.routers.achievment_router import router as achievment_router
from src.routers.auth_router import router as auth_router
from src.routers.class_router import router as class_router
from src.routers.resources_router import router as resources_router
from src.routers.task_router import router as task_router
from src.routers.submissions_router import router as submissions_router
from src.routers.premium_router import router as premium_router
from src.routers.progress_router import router_progress


# Crear todas las tablas
models.Base.metadata.create_all(bind=engine)

# Inicializar la app FastAPI
app = FastAPI()

# Habilitar el middleware CORS
orígenes = [
    "http://localhost:4200" # Reemplaza con la URL real de tu frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=orígenes,  # Especifica los orígenes permitidos
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos HTTP
    allow_headers=["*"],  # Permitir todos los encabezados
)

# Incluir los routers para diferentes funcionalidades
app.include_router(student_router)
app.include_router(achievment_router)
app.include_router(auth_router)
app.include_router(class_router)
app.include_router(resources_router)
app.include_router(task_router)
app.include_router(submissions_router)
app.include_router(premium_router)
app.include_router(router_progress)

# Ejecutar la app con Uvicorn
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
