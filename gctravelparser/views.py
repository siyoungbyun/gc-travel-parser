from flask import render_template
from gctravelparser import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/basic')
def basic():
    return render_template('basic.html')


@app.route('/advanced')
def advanced():
    return render_template('advanced.html')
