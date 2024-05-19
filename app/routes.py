from flask import render_template, url_for, flash, redirect
from app import app
from app.forms import *
from flask_login import current_user, login_user, logout_user, login_required
import sqlalchemy as sa
from app import db
from app.models import User, Post, Comment
from sqlalchemy import desc

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
@login_required
def newPost():
    form = PostForm()
    if form.validate_on_submit():
        new_post = Post(title=form.title.data, body=form.body.data, author=current_user)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('viewPosts'))
    return render_template('newPost.html', form=form)

@app.route('/viewPosts')
def viewPosts():
    posts = Post.query.order_by(desc(Post.timestamp)).all()
    return render_template('viewPosts.html', posts=posts)

@app.route('/post/<int:post_id>', methods=['GET', 'POST'])
def postDetails(post_id):
    post = Post.query.get_or_404(post_id)
    comments = Comment.query.filter_by(post_id=post_id).order_by(desc(Comment.timestamp)).all()
    form = CommentForm()

    if form.validate_on_submit():
        body = form.body.data
        comment = Comment(body=body, author=current_user, post=post)
        db.session.add(comment)
        db.session.commit()
        flash('Your comment has been added.', 'success')
        return redirect(url_for('postDetails', post_id=post_id))

    return render_template('postDetails.html', post=post, form=form, comments=comments)

@app.route('/profile/<int:user_id>')
def profile(user_id):
    posts = Post.query.filter_by(user_id=user_id).order_by(desc(Post.timestamp)).all()
    user = User.query.get_or_404(user_id)
    return render_template('profilePage.html', posts=posts, user=user)