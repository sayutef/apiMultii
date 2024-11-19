from fastapi import FastAPI
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

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(student_router)
app.include_router(achievment_router)
app.include_router(auth_router)
app.include_router(class_router)
app.include_router(resources_router)
app.include_router(task_router)
app.include_router(submissions_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)