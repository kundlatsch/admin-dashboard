from flask import abort, request

from ..auth import authenticate
from ..models.client import Client
from ..validators import validate_cpf, validate_rg, validate_date, validate_phone_number

@authenticate
def list():
    list_of_clients = Client.list_all()
    return list_of_clients

@authenticate
def insert():
    data = request.json

    name = data.get("name")
    if not name:
        return {"message": "Invalid or missing name."}, 400
    
    date_of_birth = data.get("date_of_birth", "")
    is_dob_valid = validate_date(date_of_birth)
    if not is_dob_valid:
        return {"message": "Invalid or missing date of birth."}, 400
    
    cpf = data.get("cpf", "")
    is_cpf_valid = validate_cpf(cpf)
    if not is_cpf_valid:
        return {"message": "Invalid or missing CPF."}, 400

    rg = data.get("rg", "")
    is_rg_valid = validate_rg(rg)
    if not is_rg_valid:
        return {"message": "Invalid or missing RG."}, 400
    rg_state = data.get("rg_state", "")

    phone_number = data.get("phone_number", "")
    is_phone_number_valid = validate_phone_number(phone_number)
    if not is_phone_number_valid:
        return {"message": "Invalid or missing phone number."}, 400
    
    new_client = Client(
        name,
        date_of_birth,
        cpf,
        rg,
        rg_state,
        phone_number
    )
    
    has_created = new_client.save()
    if not has_created:
        return {"message": "Fail while saving user in the database. Try again in a feel moments."}, 500
    
    return {"message": "Success."}, 200
    

@authenticate
def update(client_id: str):
    client = Client.get_by_field('id', client_id)
    if not client:
        return {"message": "User not found."}, 400
    
    data = request.json

    accepted_fields = ["name", "date_of_birth", "cpf", "rg", "rg_state", "phone_number"]
    invalid_keys = [key for key in data if key not in accepted_fields]
    for key in invalid_keys:
        del data[key]
    
    updated = client.update_fields(data)
    if not updated:
        return {"message": "Fail while updating user in the database. Try again in a feel moments."}, 500
    
    return {"message": "Success."}, 200

@authenticate
def delete(client_id: str):
    user = Client.get_by_field('id', client_id)
    if not user:
        return {"message": "User not found."}, 400

    deleted = user.delete()
    if not deleted:
        return {"message": "Fail while deleting the user from the database. Try again in a feel moments."}, 500
    
    return {"message": "Success."}, 200
