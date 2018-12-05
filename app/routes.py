from flask import Flask, render_template
from app import app, db


# Main page.
@app.route('/')
def index():
    return render_template('index.html')


# Another page.
@app.route('/page_1')
def page_1():
    return render_template('page_1.html')
