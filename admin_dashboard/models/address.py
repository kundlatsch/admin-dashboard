from copy import deepcopy
from typing import List

from ..db import fetch_one, fetch_all, execute

class Address():
    id: str
    address: str
    complement: str
    city: str
    state: str
    client_id: str


    def __init__(self, address, complement, city, state, client_id, id=None) -> None:
        # Id is optional because it is generated in the database.
        # Making it optional we can create user objects in the backend side.
        self.id = id
        self.address = address
        self.complement = complement
        self.city = city
        self.state = state
        self.client_id = client_id

    def to_dict(self):
        return deepcopy(self.__dict__)

    @staticmethod
    def get_by_field(field_name, value) -> 'Address':
        # Check if the field is a valid column in the database
        accepted_fields = ["id", "address", "complement", "city", "state", "client_id"]
        if field_name not in accepted_fields:
            return None
        
        query = f"SELECT * FROM `Addresses` WHERE `{field_name}`='{value}'"
        address = fetch_one(query)
        if not address:
            return None
        return Address(
            address.get("address"),
            address.get("complement"),
            address.get("city"),
            address.get("state"),
            address.get("client_id"),
            address.get("id")
        )
    
    @staticmethod
    def list_by_id(client_id: str) -> List['Address']:
        # TODO: add pagination
        query = f"SELECT * FROM `Addresses` WHERE `client_id`='{client_id}'"
        list_of_addresses = fetch_all(query)
        return list_of_addresses
    
    def delete(self) -> bool:
        query = f"DELETE FROM `Addresses` WHERE `id`={self.id};"
        try:
            execute(query)
            return True
        except:
            return False
    
    def update_fields(self, fields: dict) -> bool:
        update_list = []
        for field in fields:
            update_list.append(f"`{field}` = '{fields.get(field)}'")
        
        set_string = ", ".join(update_list)
        query = f"UPDATE `Addresses` SET {set_string} WHERE `id`={self.id};"
        try:
            execute(query)
            return True
        except:
            return False
    
    def save(self) -> bool:
        columns = "(`address`, `complement`, `city`, `state`, `client_id`)"
        values = f"('{self.address}', '{self.complement}', '{self.city}', '{self.state}', '{self.client_id}')"

        query = f"INSERT INTO `Addresses` {columns} VALUES {values};"
        try:
            execute(query)
            return True
        except:
            return False

    