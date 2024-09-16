import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')  # Secret key for session management
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', f'sqlite:///{os.path.join(BASE_DIR, "app.db")}')  # Database URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable track modifications
    MAIL_SERVER = 'smtp.gmail.com'  # Mail server
    MAIL_PORT = 587  # Mail server port
    MAIL_USE_TLS = True  # Use TLS for email
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')  # Mail username from environment variable
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')  # Mail password from environment variable
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER')  # Default sender email from environment variable
