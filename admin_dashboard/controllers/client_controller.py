from flask import abort, request
from passlib.hash import sha256_crypt

from ..auth import authenticate
from ..db import fetch_one
from ..models.user import User

@authenticate
def list():
    user = User.get_by_field('id', 1)
    if user: return user.to_dict()
    else: return []

def insert():
    pass

def update(client_id: str):
    pass

def delete(client_id: str):
    pass