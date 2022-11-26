from flask_bcrypt import generate_password_hash
from flask_bcrypt import check_password_hash

def set_password(user, password):
    hashed_pw = generate_password_hash(password)
    user.password = hashed_pw
    
    return user

def validate_password(user, password):
    return check_password_hash(hashed_pw, password)
    