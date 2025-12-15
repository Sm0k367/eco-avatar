from http.server import BaseHTTPRequestHandler
import json
import os

try:
    import openai
    openai.api_key = os.getenv('OPENAI_API_KEY', '')
except ImportError:
    openai = None

conversations = {}

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            
            user_message = data.get('message', '')
            session_id = data.get('session_id', 'default')
            
            if not user_message:
                self.send_error(400, 'Message is required')
                return
            
            if not openai or not openai.api_key:
                result = {
                    'success': False,
                    'error': 'OpenAI API key not configured. Please add OPENAI_API_KEY environment variable in Vercel settings.'
                }
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps(result).encode('utf-8'))
                return
            
            if session_id not in conversations:
                conversations[session_id] = [
                    {
                        "role": "system",
                        "content": "You are a helpful, friendly, and unbiased AI assistant. You provide accurate, thoughtful responses to any questions without bias or judgment. Keep your responses concise but informative."
                    }
                ]
            
            conversations[session_id].append({
                "role": "user",
                "content": user_message
            })
            
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=conversations[session_id],
                max_tokens=500,
                temperature=0.7
            )
            
            assistant_message = response.choices[0].message.content
            
            conversations[session_id].append({
                "role": "assistant",
                "content": assistant_message
            })
            
            if len(conversations[session_id]) > 21:
                conversations[session_id] = [
                    conversations[session_id][0]
                ] + conversations[session_id][-20:]
            
            result = {
                'success': True,
                'message': assistant_message,
                'session_id': session_id
            }
            
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')
            self.end_headers()
            self.wfile.write(json.dumps(result).encode('utf-8'))
            
        except Exception as e:
            error_response = {
                'success': False,
                'error': str(e)
            }
            self.send_response(500)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(error_response).encode('utf-8'))
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
