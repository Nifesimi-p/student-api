import logging
import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Configure logging
logging.basicConfig(
    level=logging.INFO,  # Can be set to DEBUG, WARNING, ERROR, etc.
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Log database connection info
logger.info("Starting Student CRUD API...")

if not app.config['SQLALCHEMY_DATABASE_URI']:
    logger.warning("DATABASE_URL not found in environment variables.")
else:
    # Avoid logging sensitive database URL in production
    logger.info(f"Connected to database: {os.getenv('DATABASE_URL') if app.config['SQLALCHEMY_DATABASE_URI'] else 'DATABASE_URL not set'}")

# Initialize database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import and register blueprints
try:
    from routes.student_routes import student_bp
    app.register_blueprint(student_bp, url_prefix='/api/v1/students')
    logger.info("Student routes registered successfully.")
except ImportError as e:
    logger.error(f"Error importing student routes: {e}")
    raise

# Healthcheck endpoint
@app.route('/api/v1/healthcheck')
def healthcheck():
    logger.info("Healthcheck endpoint called.")
    return {"status": "ok"}, 200

# Error handling for unhandled exceptions
@app.errorhandler(Exception)
def handle_error(error):
    logger.error(f"Unhandled error: {error}")
    return {"message": "Internal Server Error"}, 500

# Run the app directly
if __name__ == '__main__':
    logger.info("Running app in development mode")
    app.run(debug=True)
