from flask import Flask
from flask_sqlalchemy import flask_sqlalchemy
from datetime import datetime
app = Flask(__name__)
app.config['SQALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQALchemy(app)

class Toda(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    data_created= db.
@app.route('/')
def hello():
    return 'Hello, World!'
    