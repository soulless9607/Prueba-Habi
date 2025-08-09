import json
from http.server import BaseHTTPRequestHandler
from typing import Dict, Optional
from ..services.likes_service import LikesService
from ..core.exceptions import ValidationError, DatabaseError
import logging

logger = logging.getLogger(__name__)

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
        """Handle POST requests for adding likes"""
        try:
            # Parse request body
            data = self._parse_json()
            user_id = data.get('user_id')
            property_id = data.get('property_id')

            if not user_id or not property_id:
                raise ValidationError("user_id and property_id are required")

            # Add like
            self.service.add_like(user_id, property_id)

            # Send success response
            self.send_response(201)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            response = {"message": "Like added successfully"}
            self.wfile.write(json.dumps(response).encode())

        except ValidationError as e:
            self.send_error(400, str(e))
        except DatabaseError as e:
            self.send_error(500, str(e))
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            self.send_error(500, "Internal server error")

    def do_GET(self):
        """Handle GET requests for fetching user likes"""
        try:
            # Parse query parameters
            path_parts = self.path.split('/')
            if len(path_parts) < 3 or not path_parts[2].isdigit():
                raise ValidationError("Invalid user ID in URL")

            user_id = int(path_parts[2])
            likes = self.service.get_user_likes(user_id)

            # Send response
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"likes": likes}).encode())

        except ValidationError as e:
            self.send_error(400, str(e))
        except DatabaseError as e:
            self.send_error(500, str(e))
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            self.send_error(500, "Internal server error")