import os
from dotenv import load_dotenv

load_dotenv()

def get_database_url():
    return os.getenv("DATABASE_URL", "postgresql://user:password@localhost/dbname")