from typing import List, Dict
import logging
from ..repositories.likes_repository import LikesRepository
from ..core.exceptions import ValidationError, DatabaseError

logger = logging.getLogger(__name__)

class LikesService:
    def __init__(self, repository: LikesRepository):
        self.repository = repository

    def add_like(self, user_id: int, property_id: int) -> bool:
        """
        Add a like to a property for a specific user
        
        Args:
            user_id (int): ID of the user adding the like
            property_id (int): ID of the property being liked
            
        Returns:
            bool: True if successful, raises exception otherwise
            
        Raises:
            ValidationError: If user_id or property_id is invalid
            DatabaseError: If database operation fails
        """
        if not user_id or not property_id:
            logger.error("Invalid user_id or property_id")
            raise ValidationError("User ID and Property ID are required")

        try:
            return self.repository.add_like(user_id, property_id)
        except Exception as e:
            logger.error(f"Error adding like: {e}")
            raise

    def get_user_likes(self, user_id: int) -> List[Dict]:
        """
        Get all properties liked by a specific user
        
        Args:
            user_id (int): ID of the user
            
        Returns:
            List[Dict]: List of liked properties
            
        Raises:
            ValidationError: If user_id is invalid
            DatabaseError: If database operation fails
        """
        if not user_id:
            logger.error("Invalid user_id")
            raise ValidationError("User ID is required")

        try:
            return self.repository.get_user_likes(user_id)
        except Exception as e:
            logger.error(f"Error getting user likes: {e}")
            raise