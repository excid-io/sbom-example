import os
import secrets
from flask import Flask, jsonify
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
# Generate a secure random secret key if not provided via environment variable
app.secret_key = os.environ.get('SECRET_KEY', secrets.token_hex(32))

# Configure OAuth (basic setup for demonstration)
# This OAuth instance can be used to register OAuth providers like Google, GitHub, etc.
oauth = OAuth(app)

# Example: Uncomment to register an OAuth provider
# oauth.register(
#     name='google',
#     client_id='YOUR_GOOGLE_CLIENT_ID',
#     client_secret='YOUR_GOOGLE_CLIENT_SECRET',
#     server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
#     client_kwargs={'scope': 'openid email profile'}
# )

@app.route('/')
def index():
    """Main route that displays a welcome message."""
    return jsonify({
        'message': 'Welcome to the Flask SBOM Example App!',
        'status': 'running',
        'endpoints': {
            '/': 'This welcome message',
            '/health': 'Health check endpoint'
        }
    })

@app.route('/health')
def health():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'service': 'flask-sbom-example'
    })

if __name__ == '__main__':
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(host='0.0.0.0', port=5000, debug=debug_mode)
