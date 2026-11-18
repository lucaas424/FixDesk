from flask import Flask

from config import Config
from app.extensions import csrf, db, login_manager


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)

    from app.controllers import auth_bp, main_bp, orden_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(orden_bp)

    return app