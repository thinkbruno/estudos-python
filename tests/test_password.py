from app.services.password import generate_password

def test_password_length():
    pwd = generate_password(12)
    assert len(pwd) == 12

def test_password_is_string():
    pwd = generate_password()
    assert isinstance(pwd, str)
