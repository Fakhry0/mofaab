from flask import Flask
from app.routes.auth import auth_bp
from app.routes.main import main_bp  # Import your main blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)

    return app
