from flask import render_template, url_for, flash, redirect
from app import app
from app.forms import *
from flask_login import current_user, login_user, logout_user
import sqlalchemy as sa
from app import db
from app.models import User, Post, Comment

@app.route('/')
@app.route('/index')
def index():
    return render_template('welcomePage.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data))
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('index'))
    return render_template('loginPage.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('signUpPage.html', form=form)

@app.route('/newPost', methods=['GET', 'POST'])
def newPost():
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data
        flash(f'Title: {title}, Body: {body}', 'success')
        return redirect(url_for('index'))
    return render_template('newPost.html', form=form)