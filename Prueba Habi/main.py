from http.server import HTTPServer
import logging
from app.core import config
from app.database.connection import DatabaseConnection
from app.services import PropertyService, LikesService
from app.repositories import PropertyRepository, LikesRepository
from app.api import PropertyHandler, LikesHandler

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
    
    try:
        property_server.serve_forever()
        likes_server.serve_forever()
    except KeyboardInterrupt:
        property_server.server_close()
        likes_server.server_close()
        logger.info('Shutting down servers...')

if __name__ == '__main__':
    run_server()