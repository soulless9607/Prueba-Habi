import json
from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse
from ..repositories.property_repository import PropertyRepository
from ..core.exceptions import DatabaseError

class PropertyHandler(BaseHTTPRequestHandler):
    def __init__(self, repository: PropertyRepository, *args, **kwargs):
        self.repository = repository
        super().__init__(*args, **kwargs)

    def do_GET(self):
        try:
            # Parse query parameters
            parsed_url = urlparse(self.path)
            params = parse_qs(parsed_url.query)
            
            # Extract filters
            filters = {
                'year': int(params.get('year', [None])[0]) if params.get('year') else None,
                'city': params.get('city', [None])[0],
                'status': params.get('status', [None])[0]
            }
            
            # Get properties
            properties = self.repository.get_properties(**filters)
            
            # Send response
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(properties).encode())
            
        except DatabaseError as e:
            self.send_error(500, str(e))
        except Exception as e:
            self.send_error(400, str(e))