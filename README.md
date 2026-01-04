# sbom-example

A simple Python Flask web application demonstrating SBOM (Software Bill of Materials) generation using CycloneDX.

## Features

- **Flask Web Application**: A minimal Flask web app with basic endpoints
- **Authlib Integration**: OAuth client setup ready for integration with providers like Google, GitHub, etc.
- **Automated SBOM Generation**: GitHub Actions workflow that automatically generates CycloneDX SBOM files
- **Security Best Practices**: Environment-based configuration and secure secret key generation

## Project Structure

```
.
├── app.py                    # Flask application with routes
├── requirements.txt          # Python dependencies
├── .github/workflows/sbom.yml # GitHub Action for SBOM generation
└── README.md                 # This file
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/excid-io/sbom-example.git
   cd sbom-example
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

Start the Flask application:

```bash
python app.py
```

The application will start on `http://localhost:5000`.

For development with debug mode enabled:

```bash
FLASK_DEBUG=true python app.py
```

**Security Note**: The debug mode should never be enabled in production as it can expose sensitive information.

### Environment Variables

- `SECRET_KEY`: Set a secure secret key for Flask sessions (optional - auto-generated if not provided)
- `FLASK_DEBUG`: Set to `true` to enable debug mode (default: `false`)

Example:

```bash
export SECRET_KEY="your-secure-random-secret-key"
export FLASK_DEBUG="false"
python app.py
```

### OAuth Configuration

The application includes Authlib OAuth client setup. To configure an OAuth provider (e.g., Google, GitHub):

1. Uncomment and configure the OAuth provider in `app.py`
2. Set up your OAuth application credentials with your chosen provider
3. Add the client ID and secret to the configuration
4. Implement OAuth callback routes as needed

Example configuration is provided in `app.py` for reference.

### Available Endpoints

- `GET /` - Welcome message with API overview
- `GET /health` - Health check endpoint

## SBOM Generation

The project includes a GitHub Action that automatically generates an SBOM (Software Bill of Materials) file using CycloneDX whenever code is pushed to the main branch or a pull request is created.

### Manual SBOM Generation

To generate an SBOM locally:

```bash
pip install cyclonedx-bom
cyclonedx-py requirements requirements.txt -o sbom.json
```

This will create a `sbom.json` file containing a complete inventory of all project dependencies in CycloneDX format.

## Dependencies

- **Flask 3.0.0**: Web framework
- **Authlib 1.3.0**: OAuth library for authentication
- **Werkzeug 3.0.3**: WSGI utility library (patched version)
- **requests 2.31.0**: HTTP library

## GitHub Actions Workflow

The `.github/workflows/sbom.yml` workflow:
1. Checks out the repository
2. Sets up Python 3.11
3. Installs dependencies from `requirements.txt`
4. Generates a CycloneDX SBOM
5. Uploads the SBOM as a workflow artifact

The generated SBOM is retained for 90 days and can be downloaded from the Actions tab.

## License

This is an example project for demonstration purposes.