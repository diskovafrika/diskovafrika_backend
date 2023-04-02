from uuid import uuid4
from flask import jsonify, request
from diskovafrika.repository.v1.users import UserRepo
from diskovafrika.utils.utils import custom_response, error_response
from flasgger import swag_from


@swag_from('../../docs/create_user.yaml')
def all_users():
    """Returns all users in storage"""
    all_user = UserRepo.all_users()
    return all_user, 200


@swag_from('../../docs/create_user.yaml')
def add_user():
    request_data = request.get_json()
    id = str(uuid4())
    request_data.update({"id": id})
    validated_user = UserRepo.validate_user(request_data)
    new_user = UserRepo.create_user(validated_user)
    return custom_response(message=f"new user created", data=new_user, status_code=201)
