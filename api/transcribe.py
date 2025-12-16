from http.server import BaseHTTPRequestHandler
import json
import os
import base64
import tempfile

try:
    from openai import OpenAI
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY', ''))
    openai_available = True
except ImportError:
    client = None
    openai_available = False

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))

            audio_base64 = data.get('audio', '')

            if not audio_base64:
                self.send_error(400, 'Audio data is required')
                return

            if not openai_available or not client or not os.getenv('OPENAI_API_KEY'):
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

            # Decode base64 audio
            audio_data = base64.b64decode(audio_base64)

            # Save to temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix='.webm') as temp_audio:
                temp_audio.write(audio_data)
                temp_audio_path = temp_audio.name

            try:
                # Transcribe using Whisper
                with open(temp_audio_path, 'rb') as audio_file:
                    transcript = client.audio.transcriptions.create(
                        model="whisper-1",
                        file=audio_file
                    )

                result = {
                    'success': True,
                    'text': transcript.text
                }

                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps(result).encode('utf-8'))

            finally:
                # Clean up temp file
                if os.path.exists(temp_audio_path):
                    os.unlink(temp_audio_path)

        except Exception as e:
            result = {
                'success': False,
                'error': f'Error processing audio: {str(e)}'
            }
            self.send_response(500)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(result).encode('utf-8'))

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
