from http.server import HTTPServer
import logging
import threading
from app.core.config import config
from app.database.connection import DatabaseConnection
from app.services.property_service import PropertyService
from app.services.likes_service import LikesService
from app.repositories.property_repository import PropertyRepository
from app.repositories.likes_repository import LikesRepository
from app.api.property_handler import PropertyHandler
from app.api.likes_handler import LikesHandler

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def create_property_handler(db_connection):
    """Create a property handler with its dependencies"""
    repository = PropertyRepository(db_connection)
    service = PropertyService(repository)
    
    def handler(*args, **kwargs):
        return PropertyHandler(service, *args, **kwargs)
    return handler

def create_likes_handler(db_connection):
    """Create a likes handler with its dependencies"""
    repository = LikesRepository(db_connection)
    service = LikesService(repository)
    
    def handler(*args, **kwargs):
        return LikesHandler(service, *args, **kwargs)
    return handler

def run_server(host='localhost', port=8000):
    """Run the HTTP server"""
    db = DatabaseConnection(config.db)

    # Create server for properties endpoint
    property_server = HTTPServer(
        (host, port),
        create_property_handler(db)
    )

    # Create server for likes endpoint
    likes_server = HTTPServer(
        (host, port + 1),
        create_likes_handler(db)
    )

    logger.info(f'Starting property server on port {port}')
    logger.info(f'Starting likes server on port {port + 1}')

    def run_property_server():
        property_server.serve_forever()

    def run_likes_server():
        likes_server.serve_forever()

    property_thread = threading.Thread(target=run_property_server, daemon=True)
    likes_thread = threading.Thread(target=run_likes_server, daemon=True)

    property_thread.start()
    likes_thread.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        property_server.server_close()
        likes_server.server_close()
        logger.info('Shutting down servers...')

if __name__ == '__main__':
    run_server()