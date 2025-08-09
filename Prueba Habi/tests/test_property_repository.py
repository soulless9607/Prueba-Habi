import unittest
from unittest.mock import MagicMock, patch
from ..app.repositories.property_repository import PropertyRepository
from ..app.database.connection import DatabaseConnection
from ..app.core.config import DatabaseConfig
from ..app.core.exceptions import DatabaseError

class TestPropertyRepository(unittest.TestCase):
    def setUp(self):
        self.db_config = DatabaseConfig()
        self.db_connection = DatabaseConnection(self.db_config)
        self.repository = PropertyRepository(self.db_connection)

    def test_get_properties_success(self):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [
            {
                "id": 1,
                "address": "Test Address",
                "city": "Bogotá",
                "price": 100000,
                "year": 2020,
                "status": "en_venta"
            }
        ]

        with patch.object(self.db_connection, 'cursor') as mock_cursor_ctx:
            mock_cursor_ctx.return_value.__enter__.return_value = mock_cursor
            result = self.repository.get_properties(
                year=2020,
                city="Bogotá",
                status="en_venta"
            )
            
            self.assertEqual(len(result), 1)
            self.assertEqual(result[0]["city"], "Bogotá")

    def test_get_properties_database_error(self):
        with patch.object(self.db_connection, 'cursor') as mock_cursor_ctx:
            mock_cursor_ctx.side_effect = Exception("Database connection failed")
            
            with self.assertRaises(DatabaseError):
                self.repository.get_properties()

if __name__ == '__main__':
    unittest.main()