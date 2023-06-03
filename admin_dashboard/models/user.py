from ..db import fetch_one, execute
from copy import deepcopy

class User():
    id: str
    email: str
    name: str
    password_hash: str
    is_admin: bool

    def __init__(self, email, name, password_hash, is_admin, id=None) -> None:
        # Id is optional because it is generated in the database.
        # Making it optional we can create user objects in the backend side.
        self.id = id
        self.email = email
        self.name = name
        self.password_hash = password_hash
        self.is_admin = is_admin
    

    def to_dict(self):
        return deepcopy(self.__dict__)

    @staticmethod
    def get_by_field(field_name, value) -> 'User':
        # Check if the field is a valid column in the database
        accepted_fields = ["id", "email", "name", "password_hash", "is_admin"]
        if field_name not in accepted_fields:
            return None
        
        # Convert boolean flag to bit
        if field_name == "is_admin":
            value = 1 if value else 0
        
        query = f"SELECT * FROM `Users` WHERE `{field_name}`='{value}'"
        user = fetch_one(query)
        if not user:
            return None
        return User(
            user.get("email"),
            user.get("name"),
            user.get("password_hash"),
            user.get("is_admin"),
            user.get("id")
        )

    def save(self) -> bool:
        columns = "(`email`, `name`, `password_hash`, `is_admin`)"

        # Convert boolean flag to bit
        _is_admin = 1 if self.is_admin else 0
        values = f"('{self.email}', '{self.name}', '{self.password_hash}', '{_is_admin}')"

        query = f"INSERT INTO `Users` {columns} VALUES {values};"
        try:
            execute(query)
            return True
        except:
            return False