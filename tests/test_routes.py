import pytest
from flask import url_for
from app.models import Post

def test_new_post(test_client, init_database):
    # Log in first
    response = test_client.post('/login', data=dict(
        username='testuser',
        password='testpassword'
    ), follow_redirects=True)
    
    assert response.status_code == 200

    # Create a new post
    response = test_client.post('/newPost', data=dict(
        title='My Test Post',
        body='This is a test post body.'
    ), follow_redirects=True)

    assert response.status_code == 200
    assert b'My Test Post' in response.data
    assert b'This is a test post body.' in response.data

    # Check if the post was created in the database
    post = Post.query.filter_by(title='My Test Post').first()
    assert post is not None
    assert post.body == 'This is a test post body.'
    assert post.author.username == 'testuser'

    # Log out
    response = test_client.get('/logout', follow_redirects=True)
    assert response.status_code == 200