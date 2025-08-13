import json
from http.server import BaseHTTPRequestHandler
from typing import Dict, Optional
from ..services.likes_service import LikesService
from ..core.exceptions import ValidationError, DatabaseError
import logging

logger = logging.getLogger(__name__)
"""Tabla hipotética property_likes"""
class LikesHandler(BaseHTTPRequestHandler):
    def __init__(self, service: LikesService, *args, **kwargs):
        self.service = service
        super().__init__(*args, **kwargs)

    def _parse_json(self) -> Dict:
        """Parse JSON from request body"""
        content_length = int(self.headers.get('Content-Length', 0))
        if content_length == 0:
            return {}
            
        body = self.rfile.read(content_length)
        return json.loads(body.decode('utf-8'))

    def do_POST(self):
        logger.info("Received POST request for /likes (hypothetical property_likes table)")
        try:
            # Parse request body
            data = self._parse_json()
            logger.info(f"Parsed JSON data: {data}")
            user_id = data.get('user_id')
            property_id = data.get('property_id')

            if not user_id or not property_id:
                logger.error("Missing user_id or property_id in request")
                raise ValidationError("user_id and property_id are required")

            # Add like (hypothetical DB operation)
            logger.info(f"Attempting to add like: user_id={user_id}, property_id={property_id}")
            self.service.add_like(user_id, property_id)
            logger.info(f"Like added for user_id={user_id}, property_id={property_id} (hypothetical table)")

            # Send success response
            self.send_response(201)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            response = {"message": "Like added successfully"}
            self.wfile.write(json.dumps(response).encode())

        except ValidationError as e:
            logger.error(f"Validation error: {e}")
            self.send_error(400, str(e))
        except DatabaseError as e:
            logger.error(f"Database error: {e}")
            self.send_error(500, str(e))
        except Exception as e:
            logger.error(f"Unexpected error: {e}", exc_info=True)
            self.send_error(500, "Internal server error")

    def do_GET(self):
        """Handle GET requests for fetching user likes (hypothetical table property_likes)"""
        logger.info("Received GET request for /likes (hypothetical property_likes table)")
        try:
            # Parse query parameters
            path_parts = self.path.split('/')
            logger.info(f"Request path parts: {path_parts}")
            if len(path_parts) < 3 or not path_parts[2].isdigit():
                logger.error("Invalid user ID in URL")
                raise ValidationError("Invalid user ID in URL")

            user_id = int(path_parts[2])
            logger.info(f"Fetching likes for user_id={user_id} (hypothetical table)")
            likes = self.service.get_user_likes(user_id)
            logger.info(f"Likes fetched for user_id={user_id}: {likes}")

            # Send response
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"likes": likes}).encode())

        except ValidationError as e:
            logger.error(f"Validation error: {e}")
            self.send_error(400, str(e))
        except DatabaseError as e:
            logger.error(f"Database error: {e}")
            self.send_error(500, str(e))
        except Exception as e:
            logger.error(f"Unexpected error: {e}", exc_info=True)
            self.send_error(500, "Internal server error")