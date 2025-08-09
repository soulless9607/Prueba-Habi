from typing import List, Dict, Optional
import logging
from ..database.connection import DatabaseConnection
from ..core.exceptions import DatabaseError

logger = logging.getLogger(__name__)

class PropertyRepository:
    def __init__(self, db: DatabaseConnection):
        self.db = db

    def get_properties(
        self,
        year: Optional[int] = None,
        city: Optional[str] = None,
        status: Optional[str] = None
    ) -> List[Dict]:
        """Get properties with optional filters"""
        query = """
            SELECT DISTINCT
                p.id,
                p.address,
                p.city,
                p.price,
                p.description,
                p.year,
                s.name as status
            FROM
                property p
            INNER JOIN status_history sh ON p.id = sh.property_id
            INNER JOIN status s ON sh.status_id = s.id
            WHERE
                sh.id = (
                    SELECT MAX(id)
                    FROM status_history
                    WHERE property_id = p.id
                )
                AND s.name IN ('pre_venta', 'en_venta', 'vendido')
        """
        params = []
        
        if year:
            query += " AND p.year = %s"
            params.append(year)
        if city:
            query += " AND LOWER(p.city) = LOWER(%s)"
            params.append(city)
        if status:
            query += " AND LOWER(s.name) = LOWER(%s)"
            params.append(status)

        try:
            with self.db.cursor() as cursor:
                cursor.execute(query, params)
                return cursor.fetchall()
        except Exception as e:
            logger.error(f"Error fetching properties: {e}")
            raise DatabaseError(f"Failed to fetch properties: {str(e)}")