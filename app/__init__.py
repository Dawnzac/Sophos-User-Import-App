from flask import Flask
from .extensions import db, login_manager  # Ensure login_manager is imported
from config import Config  # Import Config explicitly
from .models import User  # Import the User model

def create_app():
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(Config)  # Use Config class directly
    
    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)  # Ensure login_manager is initialized
    
    # Configure login view
    login_manager.login_view = 'app_routes.login'
    login_manager.login_message_category = 'info'
    
    # Register blueprints
    from .routes import app_routes as main_blueprint
    app.register_blueprint(main_blueprint)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))  # Load user by ID

    return app