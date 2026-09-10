from flask import Flask


def create_app():

    app = Flask(__name__)

    from backend.routes.auth_route import auth_bp
    from backend.routes.products_route import products_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(products_bp)

    return app