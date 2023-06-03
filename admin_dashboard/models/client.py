from copy import deepcopy
from typing import List

from ..db import fetch_one, fetch_all, execute

class Client():
    id: str
    name: str
    date_of_birth: str
    cpf: str
    rg: str
    rg_state: str
    phone_number: str


    def __init__(self, name, date_of_birth, cpf, rg, rg_state, phone_number, id=None) -> None:
        # Id is optional because it is generated in the database.
        # Making it optional we can create user objects in the backend side.
        self.id = id
        self.name = name
        self.date_of_birth = date_of_birth
        self.cpf = cpf
        self.rg = rg
        self.rg_state = rg_state # state or issuing body/organization
        self.phone_number = phone_number

    def to_dict(self):
        return deepcopy(self.__dict__)

    @staticmethod
    def get_by_field(field_name, value) -> 'Client':
        # Check if the field is a valid column in the database
        accepted_fields = ["id", "name", "date_of_birth", "cpf", "rg", "rg_state", "phone_number"]
        if field_name not in accepted_fields:
            return None
        
        query = f"SELECT * FROM `Clients` WHERE `{field_name}`='{value}'"
        client = fetch_one(query)
        if not client:
            return None
        return Client(
            client.get("name"),
            client.get("date_of_birth"),
            client.get("cpf"),
            client.get("rg"),
            client.get("rg_state"),
            client.get("phone_number"),
            client.get("id")
        )
    
    def list_all() -> List['Client']:
        # TODO: add pagination
        query = f"SELECT * FROM `Clients`"
        list_of_clients = fetch_all(query)
        return list_of_clients
    
    def delete(self) -> bool:
        query = f"DELETE FROM `Clients` WHERE `id`={self.id};"
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
        query = f"UPDATE `Clients` SET {set_string} WHERE `id`={self.id};"
        try:
            execute(query)
            return True
        except:
            return False
    
    def save(self) -> bool:
        columns = "(`name`, `date_of_birth`, `cpf`, `rg`, `rg_state`, `phone_number`)"
        values = f"('{self.name}', '{self.date_of_birth}', '{self.cpf}', '{self.rg}', '{self.rg_state}', '{self.phone_number}')"

        query = f"INSERT INTO `Clients` {columns} VALUES {values};"
        try:
            execute(query)
            return True
        except:
            return False
    
    