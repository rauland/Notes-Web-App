import find
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',reminders=find.all())

@app.route("/hello")
def hello():
    return "<p>Hello, World!</p>"