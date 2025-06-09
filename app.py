from flask import Flask, jsonify, Response, request
import logging
from config import APP_VERSION
import sys

# Add the specific path to the system path
path = '/home/shubhip/CICDpipeline'
if path not in sys.path:
    sys.path.append(path)

from app import app as application

app = Flask(__name__)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)

@app.route("/")
def hello_world() -> str:
    """Root endpoint that returns a greeting.

    Returns:
        str: 'Hello World'
    """
    try:
        logger.info("Received request at '/' from %s", request.remote_addr)
        return "Hello World"
    except Exception as e:
        logger.error("Error in hello_world: %s", str(e))
        return "Internal Server Error", 500

@app.route("/health")
def health() -> Response:
    """Health check endpoint.

    Returns:
        Response: JSON response with health status.
    """
    try:
        logger.info("Received health check from %s", request.remote_addr)
        status = {"status": "ok"}
        return jsonify(status), 200
    except Exception as e:
        logger.error("Error in health endpoint: %s", str(e))
        error_status = {"status": "error", "message": str(e)}
        return jsonify(error_status), 500

@app.route("/version")
def version() -> Response:
    """Version endpoint that returns the app version from config file.

    Returns:
        Response: JSON response with app version.
    """
    try:
        logger.info("Received version check from %s", request.remote_addr)
        return jsonify({"version": APP_VERSION}), 200
    except Exception as e:
        logger.error("Error in version endpoint: %s", str(e))
        error_status = {"status": "error", "message": str(e)}
        return jsonify(error_status), 500

@app.errorhandler(Exception)
def handle_exception(e: Exception) -> Response:
    """Global error handler for unhandled exceptions.

    Args:
        e (Exception): The exception that was raised.

    Returns:
        Response: JSON response with error details.
    """
    logger.critical("Unhandled exception: %s", str(e), exc_info=True)
    response = {
        "status": "error",
        "message": "An unexpected error occurred."
    }
    return jsonify(response), 500

if __name__ == "__main__":
    app.run(debug=True)
