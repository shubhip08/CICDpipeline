# Flask CI/CD Demo

[![CI](https://github.com/<shubhip08>/<CICDpipeline>/actions/workflows/python-ci.yml/badge.svg)](https://github.com/<shubhip08>/<CICDpipeline>/actions/workflows/python-ci.yml)
[![CD](https://github.com/<shubhip08>/<CICDpipeline>/actions/workflows/python-cd.yml/badge.svg)](https://github.com/<shubhip08>/<CICDpipeline>/actions/workflows/python-cd.yml)

A simple Flask web application with CI/CD using GitHub Actions.

## Features

- `/` endpoint returns `Hello World`
- `/health` endpoint returns JSON health status
- Logging and error handling included
- Automated testing and deployment via GitHub Actions

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

```bash
git clone https://github.com/<shubhip08>/<CICDpipeline>.git
cd <CICDpipeline>
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Running the App

```bash
python app.py
```

Visit [http://localhost:5000/](http://localhost:5000/) in your browser.

### Running Tests

```bash
pytest
```

## CI/CD

- **CI:** On every push or pull request to `main`, tests and coverage are run automatically.
- **CD:** On push to `main`, the app is deployed to a remote server (see `.github/workflows/python-cd.yml`).

## Example pytest

```python
def test_hello_world(client):
    """Test the root endpoint '/'.

    Args:
        client (FlaskClient): The Flask test client.

    Asserts:
        The response status code is 200 and response data is 'Hello World'.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.data.decode() == "Hello World"
```

## License

MIT

---

**Replace `<shubhip08>` and `<CICDpipeline>` with your actual GitHub username and repository name.**
