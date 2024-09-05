from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config

db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    app.config['SECRET_KEY'] = 'your_secret_key'

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    # Redirect unauthenticated users to the login page
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Please log in to access this page.'
    login_manager.login_message_category = 'info'

    # Import and register Blueprints within the create_app function to avoid circular imports
    from .routes.auth import auth_bp
    from .routes.home import home_bp
    from .routes.main import main_bp
    from .routes.projects import projects_bp
    from app.routes.blog import blog_bp
    
    app.register_blueprint(blog_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(home_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(projects_bp)

    # Import the User model and set up the user loader after initializing extensions
    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from flask import render_template

    @app.errorhandler(403)
    def forbidden_error(error):
        return render_template('403.html'), 403

    return app
