import pytest
from flask import url_for
from app.models import User

def test_register(test_client):
    response = test_client.post('/signup', data=dict(
        username='newuser', email='newuser@example.com', password='password', password2='password'
    ), follow_redirects=True)

    assert response.status_code == 200

def test_login_logout(test_client, new_user):
    test_client.post('/signup', data=dict(
        username=new_user.username, email=new_user.email, password='testpassword', password2='testpassword'
    ), follow_redirects=True)

    response = test_client.post('/login', data=dict(
        username=new_user.username, password='testpassword'
    ), follow_redirects=True)

    assert response.status_code == 200