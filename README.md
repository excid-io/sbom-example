# SBOM generation and signing

A simple Python Flask web application demonstrating SBOM (Software Bill of Materials) generation using CycloneDX 
and signing using [cosign](https://github.com/sigstore/cosign) ans [STaaS](https://staas.excid.io/).



## Project Structure

```
.
├── app.py                    # Flask dummy application
├── requirements.txt          # Python dependencies
├── .github/workflows/sbom.yml # GitHub Action for SBOM generation and signing
└── README.md                 # This file
```



## SBOM Generation

The project includes a GitHub Action that automatically generates an SBOM 
(Software Bill of Materials) file using CycloneDX whenever code is pushed to the 
main branch or a pull request is created.


## GitHub Actions Workflow

The `.github/workflows/sbom.yml` workflow:
1. Checks out the repository
2. Sets up Python 3.11
3. Installs dependencies from `requirements.txt`
4. Generates a CycloneDX SBOM
5. Signs the SBOM using STaaS
6. Signs the SBOM using cosign
7. Uploads the SBOM as a workflow artifact

The generated SBOM is retained for 90 days and can be downloaded from the Actions tab.

## Usage
Fork the repository. Create a free account in [STaaS](https://staas.excid.io/)
and generate an API token. Then, navigate in your repository, go to Settings,
Secrets and variables, Actions and set a new Repository secret with name `STAAS_API_KEY` 

