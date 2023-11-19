from flask import Flask

def create_app():
    app = Flask(_name_)

    from .routes import init_routes
    init_routes(app)

    return app
