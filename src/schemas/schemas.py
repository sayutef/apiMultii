from pydantic import BaseModel
from datetime import date
from typing import Optional, List

class TeacherBase(BaseModel):
    name: str
    email: str
    password: str

class TeacherCreate(TeacherBase):
    pass

class Teacher(TeacherBase):
    id: int
    class Config:
        from_attributes = True

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
        from_attributes = True

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
        from_attributes = True

class ClassBase(BaseModel):
    teacher_id: int
    name: str
    description: str

class ClassCreate(ClassBase):
    pass

class Class(ClassBase):
    id: int
    class Config:
        from_attributes = True

class VideoBase(BaseModel):
    title: str
    video_url: str
    description: str

class VideoCreate(VideoBase):
    pass

class Video(VideoBase):
    id: int
    class Config:
        from_attributes = True

class EnrolledBase(BaseModel):
    student_id: int
    class_id: int

class EnrolledCreate(EnrolledBase):
    pass

class Enrolled(EnrolledBase):
    id: int
    class Config:
        from_attributes = True

class ReadingsBase(BaseModel):
    name: str
    image_url: str
    content: str

class ReadingsCreate(ReadingsBase):
    pass

class Readings(ReadingsBase):
    id: int
    class Config:
        from_attributes = True

class AchievementBase(BaseModel):
    name: str
    image_url: str

class AchievementCreate(AchievementBase):
    pass

class Achievement(AchievementBase):
    id: int
    class Config:
        from_attributes = True

class SubmissionBase(BaseModel):
    task_id: int
    student_id: int
    image_url: str

class SubmissionCreate(SubmissionBase):
    pass

class Submission(SubmissionBase):
    id: int
    class Config:
        from_attributes = True