
def test_user_exists(new_user):
    assert new_user.username == "test_user"
    assert new_user.password_hash != "test_password"