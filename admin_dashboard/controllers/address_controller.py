from flask import abort, request

from ..auth import authenticate
from ..models.address import Address
from ..models.client import Client
from ..validators import validate_cpf, validate_rg, validate_date, validate_phone_number

@authenticate
def list(client_id):
    list_of_addresses = Address.list_by_id(client_id)
    return list_of_addresses

@authenticate
def insert(client_id):
    data = request.json

    address = data.get("address")
    if not address:
        return {"message": "Invalid or missing address."}, 400
    
    client = Client.get_by_field('id', client_id)
    if not client:
        return {"message": "User not found."}, 400
    
    new_address = Address(
        address,
        data.get("complement", ""),
        data.get("city", "Cidade não informada"),
        data.get("state", "Estado não informado"),
        client.id
    )
    
    has_created = new_address.save()
    if not has_created:
        return {"message": "Fail while saving address in the database. Try again in a feel moments."}, 500
    
    return {"message": "Success."}, 200

@authenticate
def update(client_id: str, address_id: str):
    address = Address.get_by_field('id', address_id)
    if not address:
        return {"message": "Address not found."}, 400
    
    data = request.json

    accepted_fields = ["address", "complement", "city", "state"]
    invalid_keys = [key for key in data if key not in accepted_fields]
    for key in invalid_keys:
        del data[key]
    
    updated = address.update_fields(data)
    if not updated:
        return {"message": "Fail while updating user in the database. Try again in a feel moments."}, 500
    
    return {"message": "Success."}, 200

@authenticate
def delete(client_id: str, address_id: str):
    address = Address.get_by_field('id', address_id)
    if not address:
        return {"message": "User not found."}, 400

    deleted = address.delete()
    if not deleted:
        return {"message": "Fail while deleting the user from the database. Try again in a feel moments."}, 500
    
    return {"message": "Success."}, 200
