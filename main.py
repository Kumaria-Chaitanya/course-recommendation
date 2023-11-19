# main.py

from flask import Flask
from db.databases import init_db

app = Flask(__name__)

# Initialize the database
init_db(app)

# ... (your existing routes and logic)

if __name__ == '__main__':
    app.run(debug=True)
