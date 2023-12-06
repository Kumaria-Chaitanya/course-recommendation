from flask import Flask
from db.databases import init_db

def create_app():
    app = Flask(__name__)

    # Initialize the database
    init_db(app)

    from .routes import init_routes
    init_routes(app)

    return app
