from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config
from flask_mail import Mail
import os

# Initialize extensions
db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()
mail = Mail()

def create_app():
    app = Flask(__name__, static_folder='static', template_folder='templates')
    app.config.from_object('app.config.Config')  # Load configuration from Config class
    app.config['SECRET_KEY'] = 'your_secret_key'  # Secret key for session management
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Database URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable track modifications
    app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static/uploads')  # Upload folder path
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB max file size

    # Initialize extensions with the app instance
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)

    # Redirect unauthenticated users to the login page
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Please log in to access this page.'
    login_manager.login_message_category = 'info'

    # Import and register Blueprints within the create_app function to avoid circular imports
    from .routes.auth import auth_bp
    from .routes.home import home_bp
    from .routes.main import main_bp
    from .routes.projects import projects_bp
    from .routes.blog import blog_bp
    from .routes.profile import profile_bp
    from .routes.contact import contact_bp
    from .routes.admin import admin_bp
    
    app.register_blueprint(blog_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(home_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(projects_bp)
    app.register_blueprint(profile_bp)
    app.register_blueprint(contact_bp)
    app.register_blueprint(admin_bp)

    # Import the User model and set up the user loader after initializing extensions
    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))  # Load user by ID

    return app
