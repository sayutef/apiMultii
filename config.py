from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/dbname")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

#MONGODB_URL = os.getenv("MONGODB_URL", "mongodb+srv://sayu:sayu123@letroapi.mgwg8.mongodb.net/")
#mongo_client = MongoClient(MONGODB_URL)

# Especifica el nombre de la base de datos explícitamente
#mongo_db_name = "letroapi"  # Cambia esto por el nombre real
#mongo_db = mongo_client.get_database(mongo_db_name)

