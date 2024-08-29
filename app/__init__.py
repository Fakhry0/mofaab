from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    app.config['SECRET_KEY'] = 'your_secret_key'

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    # Import and register Blueprints within the create_app function to avoid circular imports
    from .routes.auth import auth_bp
    from .routes.home import home_bp  # assuming you have a home blueprint
    from .routes.main import main_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(home_bp)
    app.register_blueprint(main_bp)

    return app

# Move this import after the app and extensions have been initialized to avoid circular import issues
from .models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
