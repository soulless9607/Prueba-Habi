from typing import List, Dict, Optional
import logging
from ..repositories.property_repository import PropertyRepository
from ..models.property import PropertyResponse

logger = logging.getLogger(__name__)

class PropertyService:
    def __init__(self, repository: PropertyRepository):
        self.repository = repository
    
    def get_properties(
        self,
        year: Optional[int] = None,
        city: Optional[str] = None,
        status: Optional[str] = None
    ) -> List[Dict]:
        try:
            return self.repository.get_properties(
                year=year,
                city=city,
                status=status
            )
        except Exception as e:
            logger.error(f"Error getting properties: {e}")
            raise