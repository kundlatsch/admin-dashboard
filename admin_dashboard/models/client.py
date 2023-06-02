from typing import List

class Client():
    id: str
    name: str
    date_of_birth: str
    cpf: str
    rg: str
    rg_state: str
    phone_number: str


    def __init__(self, id, name, date_of_birth, cpf, rg, rg_state, phone_number) -> None:
        self.id = id
        self.name = name
        self.date_of_birth = date_of_birth
        self.cpf = cpf
        self.rg = rg
        self.rg_state = rg_state
        self.phone_number = phone_number

    @staticmethod
    def get_by_id(id: str) -> 'Client':
        # make query to get user from database
        return Client(None, None, None, None, None, None, None)
    
    def list_all() -> List['Client']:
        # make query to get all clients
        return []
    
    @staticmethod
    def delete_by_id(id: str) -> bool:
        # make query to delete user from the database
        return True
    
    def update_fields(fields: dict) -> bool:
        for field in fields:
            # build query
            pass
        # make query to update user
        return True
    
    def save() -> bool:
        # make query to insert in the database
        return True
    
    