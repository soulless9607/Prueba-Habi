import unittest
from unittest.mock import MagicMock, patch
from ..app.services.likes_service import LikesService
from ..app.repositories.likes_repository import LikesRepository
from ..app.core.exceptions import ValidationError, DatabaseError

class TestLikesService(unittest.TestCase):
    def setUp(self):
        self.repository = MagicMock(spec=LikesRepository)
        self.service = LikesService(self.repository)

    def test_add_like_success(self):
        # Arrange
        user_id = 1
        property_id = 2
        self.repository.add_like.return_value = True

        # Act
        result = self.service.add_like(user_id, property_id)

        # Assert
        self.assertTrue(result)
        self.repository.add_like.assert_called_once_with(user_id, property_id)

    def test_add_like_invalid_input(self):
        # Test with invalid user_id
        with self.assertRaises(ValidationError):
            self.service.add_like(None, 1)

        # Test with invalid property_id
        with self.assertRaises(ValidationError):
            self.service.add_like(1, None)

    def test_add_like_database_error(self):
        # Arrange
        self.repository.add_like.side_effect = DatabaseError("Database error")

        # Act & Assert
        with self.assertRaises(DatabaseError):
            self.service.add_like(1, 1)

    def test_get_user_likes_success(self):
        # Arrange
        user_id = 1
        expected_likes = [
            {
                "property_id": 1,
                "address": "Test Address",
                "created_at": "2023-08-09"
            }
        ]
        self.repository.get_user_likes.return_value = expected_likes

        # Act
        result = self.service.get_user_likes(user_id)

        # Assert
        self.assertEqual(result, expected_likes)
        self.repository.get_user_likes.assert_called_once_with(user_id)

    def test_get_user_likes_invalid_user(self):
        with self.assertRaises(ValidationError):
            self.service.get_user_likes(None)

    def test_get_user_likes_database_error(self):
        # Arrange
        self.repository.get_user_likes.side_effect = DatabaseError("Database error")

        # Act & Assert
        with self.assertRaises(DatabaseError):
            self.service.get_user_likes(1)

if __name__ == '__main__':
    unittest.main()