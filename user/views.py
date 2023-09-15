from flask import Blueprint, request
from user.model import User
import datetime as dt
from exceptions import InvalidUsage
from flasgger.utils import swag_from

blueprint = Blueprint('user', __name__)

@swag_from("../swagger/user/list_users.yaml")
@blueprint.route('/api/user', methods=(['GET']))
def get_user():
    serializedUsers = []

    for user in User.query.all():
        serializedUsers.append(user.serialize())

    return serializedUsers

@swag_from("../swagger/user/register_user.yaml")
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
    user.set_updated_at(dt.datetime.utcnow)
    return user.save().serialize()

@blueprint.route("/api/user/<int:id>", methods=(['DELETE']))
def delete_user(id):
    user = find_user_by_id(id)

    user.delete()
    return '', 200

@blueprint.route("/api/user/deposit/<int:id>", methods=(['PATCH']))
def add_user_money(id):
    quantity = request.json["quantity"]

    user = find_user_by_id(id)
    user.add_money(quantity)
    user.set_updated_at(dt.datetime.utcnow())

    return user.save().serialize()

def find_user_by_id(user_id):
    found_user = User.query.get(user_id)
    if found_user is None:
        raise InvalidUsage.user_not_found()
    return found_user

