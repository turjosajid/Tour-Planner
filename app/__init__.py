from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = '11235813'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tourplanner.db"

db = SQLAlchemy(app)

from app import routes

