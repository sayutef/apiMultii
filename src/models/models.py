from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey, BigInteger
from sqlalchemy.orm import relationship
from config import Base

class Teacher(Base):
    __tablename__ = "teacher"
    id = Column(BigInteger, primary_key=True)
    name = Column(String(45))
    email = Column(String(150))
    password = Column(String(255))
    classes = relationship("Class", back_populates="teacher")

class Student(Base):
    __tablename__ = "student"
    id = Column(BigInteger, primary_key=True)
    name = Column(String(20))
    paternal_surname = Column(String(25))
    maternal_surname = Column(String(25))
    registration_number = Column(BigInteger, unique=True, index=True)
    password = Column(String(255))
    enrollments = relationship("Enrolled", back_populates="student")
    submissions = relationship("Submission", back_populates="student")  

class Task(Base):
    __tablename__ = "task"
    id = Column(BigInteger, primary_key=True)
    class_id = Column(BigInteger, ForeignKey("class.id"))
    name = Column(String(100))
    act_number = Column(BigInteger)
    due_date = Column(Date)
    description = Column(String(500))
    class_task = relationship("Class", back_populates="tasks")
    submissions = relationship("Submission", back_populates="task")

class Class(Base):
    __tablename__ = "class"
    id = Column(BigInteger, primary_key=True)
    teacher_id = Column(BigInteger, ForeignKey("teacher.id"))
    name = Column(String(35))
    description = Column(String(500))
    teacher = relationship("Teacher", back_populates="classes")
    enrollments = relationship("Enrolled", back_populates="class_")
    tasks = relationship("Task", back_populates="class_task")

class Video(Base):
    __tablename__ = "video"
    id = Column(BigInteger, primary_key=True)
    title = Column(String(45))
    video_url = Column(String(600))
    description = Column(Text)

class Numbers(Video):
    __tablename__ = "numbers"
    id = Column(BigInteger, ForeignKey("video.id"), primary_key=True)

class WriteAndRead(Video):
    __tablename__ = "write_and_read"
    id = Column(BigInteger, ForeignKey("video.id"), primary_key=True)

class Enrolled(Base):
    __tablename__ = "enrolled"
    id = Column(BigInteger, primary_key=True)
    student_id = Column(BigInteger, ForeignKey("student.id"))
    class_id = Column(BigInteger, ForeignKey("class.id"))
    student = relationship("Student", back_populates="enrollments")
    class_ = relationship("Class", back_populates="enrollments")

class Readings(Base):
    __tablename__ = "readings"
    id = Column(BigInteger, primary_key=True)
    name = Column(String(45))
    image_url = Column(String(600))
    content = Column(Text)

class Achievement(Base):
    __tablename__ = "achievement"
    id = Column(BigInteger, primary_key=True)
    name = Column(String(45))
    image_url = Column(String(600))

class Submission(Base):
    __tablename__ = "submission"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    task_id = Column(BigInteger, ForeignKey("task.id"), nullable=False)
    student_id = Column(BigInteger, ForeignKey("student.id"), nullable=False)
    image_url = Column(String(600))
    
    task = relationship("Task", back_populates="submissions")
    student = relationship("Student", back_populates="submissions")

# class Numbers(Video):
#     __tablename__ = "numbers"

# class WriteAndRead(Video):
#     __tablename__ = "write_and_read"