from pydantic import BaseModel,  validator
from datetime import date, datetime
from typing import Optional, List
from bson import ObjectId


class TeacherBase(BaseModel):
    name: str
    email: str
    password: str


class TeacherCreate(TeacherBase):
    pass


class Teacher(TeacherBase):
    id: int

    class Config:
        from_attributes = True  # Pydantic V2: `orm_mode` cambiado a `from_attributes`


class StudentBase(BaseModel):
    name: str
    paternal_surname: str
    maternal_surname: str
    registration_number: int
    password: str


class StudentCreate(StudentBase):
    pass


class Student(StudentBase):
    id: int

    class Config:
        from_attributes = True  # Pydantic V2: `orm_mode` cambiado a `from_attributes`


class TaskBase(BaseModel):
    name: str
    class_id: int
    act_number: int
    due_date: date
    description: str


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: int

    class Config:
        from_attributes = True  # Pydantic V2: `orm_mode` cambiado a `from_attributes`


class ClassBase(BaseModel):
    id: int
    name: str
    description: str


class ClassCreate(ClassBase):
    pass


class Class(ClassBase):
    id: int

    class Config:
        from_attributes = True  # Pydantic V2: `orm_mode` cambiado a `from_attributes`


class VideoBase(BaseModel):
    title: str
    video_url: str
    description: str


class VideoCreate(VideoBase):
    pass


class Video(VideoBase):
    id: int

    class Config:
        from_attributes = True  # Pydantic V2: `orm_mode` cambiado a `from_attributes`


class EnrolledBase(BaseModel):
    student_id: int
    class_id: int


class EnrolledCreate(EnrolledBase):
    pass


class Enrolled(EnrolledBase):
    id: int

    class Config:
        from_attributes = True  # Pydantic V2: `orm_mode` cambiado a `from_attributes`


class ReadingsBase(BaseModel):
    name: str
    image_url: str
    content: str


class ReadingsCreate(ReadingsBase):
    pass


class Readings(ReadingsBase):
    id: int

    class Config:
        from_attributes = True  # Pydantic V2: `orm_mode` cambiado a `from_attributes`


class AchievementBase(BaseModel):
    name: str
    image_url: str


class AchievementCreate(AchievementBase):
    pass


class Achievement(AchievementBase):
    id: int

    class Config:
        from_attributes = True  # Pydantic V2: `orm_mode` cambiado a `from_attributes`


class SubmissionBase(BaseModel):
    task_id: int
    student_id: int
    image_url: str


class SubmissionCreate(SubmissionBase):
    pass


class Submission(SubmissionBase):
    id: int

    class Config:
        from_attributes = True  # Pydantic V2: `orm_mode` cambiado a `from_attributes`


# MongoDB Models
class Progress(BaseModel):
    subject: Optional[str]  # Asignatura
    progress: int  # Progreso en porcentaje
    student_id: str  # ID del estudiante
    createdAt: Optional[datetime] = datetime.utcnow()  # Fecha de creación del progreso

    def dict(self, *args, **kwargs):
        data = super().dict(*args, **kwargs)
        if 'createdAt' in data:
            if isinstance(data['createdAt'], datetime):
                data['createdAt'] = data['createdAt'].strftime("%Y-%m-%d")
        return data

class PremiumBase(BaseModel):
    student_id: int  
    is_active: bool


class PremiumCreate(BaseModel):
    student_id: int  
    is_active: bool

class Premium(PremiumCreate):
    id: int 

    class Config:
        from_attributes = True
        json_encoders = {
            ObjectId: int
        }
