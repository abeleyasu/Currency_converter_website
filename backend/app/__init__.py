from flask import Flask
from .auth import auth_bp

def create_app():
    app = Flask(__name__)
    
    # Configurations can be added here
    
    app.register_blueprint(auth_bp)
    
    return app
