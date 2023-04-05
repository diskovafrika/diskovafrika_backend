from uuid import uuid4
from flask import jsonify, request
from diskovafrika.repository.v1.users import UserRepo
from diskovafrika.utils.utils import custom_response, error_response
from flasgger import swag_from


@swag_from('../../docs/users_all.yaml')
def all_users():
    """
    The all_users function returns a list of all users in the database.
        ---
        tags:
          - Users API

    :return: All users in the database

    """

    all_user = UserRepo.all_users()
    return all_user, 200


@swag_from('../../docs/users.yaml')
def add_user():
    """
    The add_user function creates a new user in the database.
        ---
        tags:
          - User API

    :return: A custom response with a message, the data and status code

    """
    request_data = request.get_json()
    id = str(uuid4())
    request_data.update({"id": id})
    validated_user = UserRepo.validate_user(request_data)
    new_user = UserRepo.create_user(validated_user)
    return custom_response(message=f"new user created", data=new_user, status_code=201)
