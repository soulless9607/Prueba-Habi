from typing import Generator
from fastapi import Depends
from sqlalchemy.orm import Session
from app.repositories.property_repository import PropertyRepository
from app.services.property_service import PropertyService

def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_property_repository(
    db: Session = Depends(get_db)
) -> PropertyRepository:
    return PropertyRepository(db)

def get_property_service(
    repository: PropertyRepository = Depends(get_property_repository)
) -> PropertyService:
    return PropertyService(repository)