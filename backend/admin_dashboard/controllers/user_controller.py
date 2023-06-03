import jwt
from flask import abort, request, current_app
from passlib.hash import sha256_crypt

from ..auth import authenticate
from ..db import fetch_one
from ..models.user import User
from ..validators import validate_email


def insert():
    data = request.json

    email = data.get("email")
    if not email or not validate_email(email):
        return {"message": "Invalid email address."}, 400
    user = User.get_by_field('email', email)
    if user:
        return {"message": "Email already in use."}, 400

    password = data.get("password")
    if len(password) < 8:
        return {"message": "Your password must be at least 8 characters long."}, 400 
    
    password_hash = sha256_crypt.encrypt(password)

    name = data.get("name", "")
    is_admin = data.get("is_admin", False)
    new_user = User(email, name, password_hash, is_admin)

    has_created = new_user.save()
    if not has_created:
        return {"message": "Fail while saving user in the database. Try again in a feel moments."}, 500
    
    return {"message": "Success."}, 200
    

def login():
    data = request.json
    email = data.get("email")
    user = User.get_by_field('email', email)

    if not user:
        return {"message": "Email or password is invalid."}, 400

    password = data.get("password")
    valid_login = sha256_crypt.verify(password, user.password_hash)

    if not valid_login:
        return {"message": "Email or password is invalid."}, 400
    
    secret = current_app.config['SECRET_KEY']
    jwt_token = jwt.encode({"id": user.id}, secret, algorithm="HS256")

    return {"token": jwt_token}