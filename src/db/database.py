import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pymongo import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient
import logging

# Configuración de logging
logging.basicConfig(level=logging.INFO)

# Cargar variables de entorno
load_dotenv()

# Configuración de MongoDB (con pymongo y motor para soporte asíncrono)
MONGODB_URL = os.getenv("MONGODB_URL")
if not MONGODB_URL:
    raise ValueError("MONGODB_URL no está configurado en el archivo .env")

logging.info(f"Connecting to MongoDB with URL: {MONGODB_URL}")
mongo_client = MongoClient(MONGODB_URL)  # Conexión síncrona
mongo_db = mongo_client["letroapi"]

async_mongo_client = AsyncIOMotorClient(MONGODB_URL)  # Conexión asíncrona
async_mongo_db = async_mongo_client["letroapi"]

# Configuración de PostgreSQL
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL no está configurado en el archivo .env")

logging.info(f"Connecting to PostgreSQL with URL: {DATABASE_URL}")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_mongo_db():
    return mongo_db


def get_async_mongo_db():
    return async_mongo_db


