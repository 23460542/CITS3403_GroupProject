def test_new_user(new_user):
    assert new_user.username == 'testuser'
    assert new_user.email == 'testuser@example.com'
    assert new_user.check_password('testpassword') == True

def test_new_post(new_post):
    assert new_post.title == 'Test Post'
    assert new_post.body == 'This is a test post.'

def test_new_comment(new_comment):
    assert new_comment.body == 'This is a test comment.'
