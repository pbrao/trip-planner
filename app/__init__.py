from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///travel.db'
    app.config['SECRET_KEY'] = 'your-secret-key'
    
    db.init_app(app)
    
    from app.routes import main_routes
    app.register_blueprint(main_routes)
    
    with app.app_context():
        db.create_all()
    
    return app
