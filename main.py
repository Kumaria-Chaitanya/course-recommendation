# main.py

from flask import Flask
from db.databases import db

app = Flask(__name__)

# ... (your existing routes and logic)
from api.routes import *

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True, port=3000)