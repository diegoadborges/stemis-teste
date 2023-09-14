from flask import Blueprint, request
from user.model import User


blueprint = Blueprint('user', __name__)

@blueprint.route('/api/user', methods=(['GET']))
def get_user():
    serializedUsers = []

    for user in User.query.all():
        serializedUsers.append(user.serialize())

    return serializedUsers

@blueprint.route('/api/user/register', methods=(['POST']))
def create_user():
    username = request.json["name"]
    return User(username).save().serialize()

@blueprint.route("/api/user/update", methods=(['PUT']))
def update_user():
    user_id = request.json["id"]
    username = request.json["username"]

    user = find_user_by_id(user_id)
    
    user.set_name(username)
    return user.save().serialize()

@blueprint.route("/api/user/<id>", methods=(['DELETE']))
def delete_user(id):
    user = find_user_by_id(id)

    user.delete()
    return '', 200

@blueprint.route("/api/user/deposit/<id>", methods=(['PATCH']))
def add_user_money(id):
    quantity = request.json["quantity"]

    user = find_user_by_id(id)
    user.add_money(quantity)

    return user.serialize()

def find_user_by_id(user_id):
    found_user = User.query.get(user_id)
    if found_user is None:
        print("not found")
        # TODO create exception when user is not found
        return 
    return found_user

