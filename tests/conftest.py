import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import pytest
from app import app, db
from config import TestConfig
from app.models import User, Post, Comment

@pytest.fixture(scope='module')
def test_client():
    app.config.from_object(TestConfig)

    with app.test_client() as testing_client:
        with app.app_context():
            db.create_all()
            yield testing_client
            db.drop_all()

@pytest.fixture(scope='module')
def new_user():
    user = User(username='testuser', email='testuser@example.com')
    user.set_password('testpassword')
    return user

@pytest.fixture(scope='module')
def new_post(new_user):
    post = Post(title='Test Post', body='This is a test post.', author=new_user)
    return post

@pytest.fixture(scope='module')
def new_comment(new_user, new_post):
    comment = Comment(body='This is a test comment.', author=new_user, post=new_post)
    return comment

@pytest.fixture(scope='module')
def init_database():
    db.create_all()

    user1 = User(username='testuser', email='testuser@example.com')
    user1.set_password('testpassword')
    db.session.add(user1)

    post1 = Post(title='Test Post 1', body='This is a test post', author=user1)
    post2 = Post(title='Test Post 2', body='This is another test post', author=user1)
    db.session.add(post1)
    db.session.add(post2)

    db.session.commit()

    yield db

    db.drop_all()
