from typing import Dict, Optional
import logging
from ..database.connection import DatabaseConnection
from ..core.exceptions import DatabaseError

logger = logging.getLogger(__name__)

class LikesRepository:
    def __init__(self, db: DatabaseConnection):
        self.db = db

    def add_like(self, user_id: int, property_id: int) -> bool:
        """Add a like to a property"""
        query = """
            INSERT INTO property_likes (user_id, property_id, created_at)
            VALUES (%s, %s, NOW())
        """
        
        try:
            with self.db.cursor() as cursor:
                cursor.execute(query, (user_id, property_id))
                return True
        except Exception as e:
            logger.error(f"Error adding like: {e}")
            raise DatabaseError(f"Failed to add like: {str(e)}")

    def get_user_likes(self, user_id: int) -> Dict:
        """Get all likes for a user"""
        query = """
            SELECT pl.*, p.address
            FROM property_likes pl
            JOIN property p ON pl.property_id = p.id
            WHERE pl.user_id = %s
        """
        
        try:
            with self.db.cursor() as cursor:
                cursor.execute(query, (user_id,))
                return cursor.fetchall()
        except Exception as e:
            logger.error(f"Error fetching user likes: {e}")
            raise DatabaseError(f"Failed to fetch user likes: {str(e)}")