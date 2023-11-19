from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Change this URL based on your database
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    with app.app_context():
        db.create_all()