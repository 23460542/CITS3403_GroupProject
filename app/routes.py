from flask import render_template, url_for, flash, redirect
from app import app
from app.forms import *

@app.route('/')
@app.route('/index')
def index():
    return render_template('welcomePage.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}'.format(
            form.username.data))
        return redirect(url_for('index'))
    return render_template('loginPage.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        flash('Signup requested for user {}'.format(
            form.username.data))
        return redirect(url_for('index'))
    return render_template('signUpPage.html', form=form)