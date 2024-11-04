# backend/app.py

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def index():
    return "Welcome to the Brent Oil Price Analysis API!"

if __name__ == '__main__':
    app.run(debug=True)
