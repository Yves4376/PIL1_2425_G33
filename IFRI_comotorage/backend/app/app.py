from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    CORS(app)

    # Import routes
    from routes.auth import auth_bp
    from routes.rides import rides_bp
    from routes.messaging import messaging_bp

    # Register Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(rides_bp)
    app.register_blueprint(messaging_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
