from flask import render_template, url_for
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('Welcome.html')

@app.route('/pfp')
def pfp():
    return render_template('profilePage.html')