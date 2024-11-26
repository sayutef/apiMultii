import os
from dotenv import load_dotenv

load_dotenv()

def get_database_url():
    return os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost/letroapi")

def get_mongodb_url():
    return os.getenv("MONGODB_URL", "mongodb://localhost:27017/letroapi")