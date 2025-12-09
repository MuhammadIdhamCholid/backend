from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings  

# Create the database engine
engine = create_engine(settings.DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Base model untuk inheritance di semua model ORM
Base = declarative_base()

# Dependency untuk mendapatkan session (dipanggil di router)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
