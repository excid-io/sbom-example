import os
from flask import Flask, jsonify
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'development-secret-key-change-in-production')

# Configure OAuth (basic setup for demonstration)
oauth = OAuth(app)

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
