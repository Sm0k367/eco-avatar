from http.server import BaseHTTPRequestHandler
import json
from datetime import datetime
import os

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        api_key_set = bool(os.getenv('OPENAI_API_KEY'))
        
        result = {
            'status': 'healthy',
            'timestamp': datetime.now().isoformat(),
            'platform': 'vercel',
            'message': 'AI Avatar API is running',
            'openai_configured': api_key_set
        }
        
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(result).encode('utf-8'))
