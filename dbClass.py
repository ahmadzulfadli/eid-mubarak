from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, redirect, request
from datetime import date, timedelta

# objek flask
app = Flask(__name__)

# koneksi ke database


app.config["SQLALCHEMY_DATABASE_URI"] = userpass + basedir + dbname
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# tabel Pesan
class Pesan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.current_timestamp())

    def __init__(self, text):
        self.text = text