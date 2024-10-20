from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# SQLAlchemy database URL (from config settings)
DATABASE_URL = settings.DATABASE_URL

# Create the engine that will connect to the database
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class for database transactions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declare the Base class for the ORM models
Base = declarative_base()

# Dependency: get a database session for each request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# def create_tables():
#     Base.metadata.create_all(bind=engine)

