# main.py

from flask import Flask
from db.databases import init_db

app = Flask(__name__)

# ... (your existing routes and logic)
from api.routes import *

if __name__ == '__main__':
    init_db(app)  # Initialize the database
    app.run(debug=True, port=3000)