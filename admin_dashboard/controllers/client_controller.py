from ..auth import authenticate

from ..db import fetch_one

# @authenticate
def list():
    result = fetch_one("SELECT `email` FROM `Users` WHERE `id`=1")
    if result: return result
    else: return []

def insert():
    pass

def update(client_id: str):
    pass

def delete(client_id: str):
    pass