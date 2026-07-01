from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

# 1. Configure the SQLite connection URL
DATABASE_URL = "sqlite:///./carbon_tracker.db"

# 2. Create the engine and session factory
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 3. Establish the declarative base class for our models
Base = declarative_base()

# 4. Define the Activities table schema
class ActivityLogModel(Base):
    __tablename__ = "activity_logs"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow, index=True)
    category = Column(String, nullable=False)       # e.g., 'commute'
    subcategory = Column(String, nullable=False)    # e.g., 'bus'
    value = Column(Float, nullable=False)           # e.g., 600.0
    calculated_co2e = Column(Float, nullable=False) # e.g., 19.2

# Helper function to generate tables on startup
def init_db():
    Base.metadata.create_all(bind=engine)