from flask import Blueprint, request
from user.model import User


blueprint = Blueprint('user', __name__)

@blueprint.route('/api/users', methods=(['GET']))
def get_user():
    serializedUsers = []

    for user in User.query.all():
        serializedUsers.append(user.serialize())

    return serializedUsers

@blueprint.route('/api/users/register', methods=(['POST']))
def create_user():
    username = request.json["name"]
    return User(username).save().serialize()

@blueprint.route("/api/users/update", methods=(['PUT']))
def update_user():
    user_id = request.json["id"]
    username = request.json["username"]

    user = find_user_by_id(user_id)
    
    user.set_name(username)
    return user.save().serialize()

@blueprint.route("/api/users/<id>", methods=(['DELETE']))
def delete_user(id):
    user = find_user_by_id(id)
    
    user.delete()
    return '', 200

def find_user_by_id(user_id):
    found_user = User.query.get(user_id)
    if found_user is None:
        print("not found")
        # TODO create exception when user is not found
        return 
    return found_user