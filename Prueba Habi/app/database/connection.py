from contextlib import contextmanager
import mysql.connector
from mysql.connector.cursor import MySQLCursor
from typing import Generator
import logging
from ..core.config import DatabaseConfig

logger = logging.getLogger(__name__)

class DatabaseConnection:
    def __init__(self, config: DatabaseConfig):
        self.config = config
        self._connection = None

    def connect(self) -> None:
        try:
            self._connection = mysql.connector.connect(
                host=self.config.host,
                port=self.config.port,
                user=self.config.user,
                password=self.config.password,
                schema=self.config.schema
            )
        except mysql.connector.Error as e:
            logger.error(f"Error connecting to database: {e}")
            raise

    @contextmanager
    def cursor(self) -> Generator[MySQLCursor, None, None]:
        if not self._connection or not self._connection.is_connected():
            self.connect()
            
        cursor = self._connection.cursor(dictionary=True)
        try:
            yield cursor
            self._connection.commit()
        except mysql.connector.Error as e:
            self._connection.rollback()
            logger.error(f"Database error: {e}")
            raise
        finally:
            cursor.close()

    def close(self) -> None:
        if self._connection:
            self._connection.close()