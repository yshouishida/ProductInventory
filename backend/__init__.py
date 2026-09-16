from flask import Flask
from werkzeug.exceptions import HTTPException

from backend.utils.api_response import error


def create_app():

    app = Flask(__name__)

    from backend.routes.auth_route import auth_bp
    from backend.routes.products_route import products_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(products_bp)

    @app.errorhandler(Exception)
    def handle_error(exc):
        if isinstance(exc, HTTPException):
            return error(exc.description, exc.code)
        app.logger.exception("Request failed")
        return error("Internal server error.", 500)

    return app
