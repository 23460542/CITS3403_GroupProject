import os
import unittest
from datetime import datetime, timezone
from app import app, db
from app.models import User, Post
from flask import url_for

os.environ['DATABASE_URL'] = 'sqlite://'

class UserModelCase(unittest.TestCase):
    def setUp(self):
        self.app_context = app.app_context()
        self.app_context.push()
        self.client = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_password_hashing(self):
        u = User(username='susan', email='susan@example.com')
        u.set_password('cat')
        self.assertFalse(u.check_password('dog'))
        self.assertTrue(u.check_password('cat'))

    def test_post(self):
        u = User(username='susan', email='susan@example.com')
        u.set_password('cat')
        db.session.add(u)
        db.session.commit()
        p = Post(title='Test', body='Test body', author=u)
        db.session.add(p)
        db.session.commit()
        self.assertEqual(p.author.username, 'susan')

    def test_signup(self):
        response = self.client.post('/signup', data={
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'password',
            'password2': 'password'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        u = User(username='testuser', email='testuser@example.com')
        u.set_password('password')
        db.session.add(u)
        db.session.commit()
        response = self.client.post('/login', data={
            'username': 'testuser',
            'password': 'password'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main(verbosity=2)
