from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, redirect, request
from datetime import date, timedelta

# objek flask
app = Flask(__name__)

# koneksi ke database

db = SQLAlchemy(app)

# tabel komposter
class Pesan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.current_timestamp())

    def __init__(self, text):
        self.text = text
