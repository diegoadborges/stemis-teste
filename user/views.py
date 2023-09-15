from flask import Blueprint, request
from user.model import User
import datetime as dt
from exceptions import InvalidUsage
from flasgger.utils import swag_from

blueprint = Blueprint('user', __name__)

@swag_from("../docs/user/list_users.yaml")
@blueprint.route('/api/user', methods=(['GET']))
def get_user():
    page = request.args.get("page")
    per_page = request.args.get("per_page")
    if page is None:
        page = 1
    if per_page is None:
        per_page = 5

    serializedUsers = []
    try:
        per_page = int(per_page)
        page = int(page)
        for user in User.query.paginate(per_page=per_page, page=page):
            serializedUsers.append(user.serialize())
    except:
        InvalidUsage.invalid_value()

    return serializedUsers

@swag_from("../docs/user/register_user.yaml")
@blueprint.route('/api/user/register', methods=(['POST']))
def create_user():
    username = request.json["name"]

    if User.query.filter_by(name = username).first() is not None:
        raise InvalidUsage.username_exists()

    return User(username).save().serialize()

@swag_from("../docs/user/update_user.yaml")
@blueprint.route("/api/user/update", methods=(['PUT']))
def update_user():
    user_id = request.json["id"]
    username = request.json["username"]

    user = find_user_by_id(user_id)
    
    user.set_name(username)
    user.set_updated_at(dt.datetime.utcnow())
    return user.save().serialize()

@swag_from("../docs/user/delete_user.yaml")
@blueprint.route("/api/user/<int:id>", methods=(['DELETE']))
def delete_user(id):
    user = find_user_by_id(id)

    user.delete()
    return '', 200

@swag_from("../docs/user/deposit_user.yaml")
@blueprint.route("/api/user/deposit/<int:id>", methods=(['PATCH']))
def add_user_money(id):
    quantity = request.json["quantity"]
    
    if quantity <= 0:
        raise InvalidUsage.invalid_operation()

    user = find_user_by_id(id)
    user.add_money(quantity)
    user.set_updated_at(dt.datetime.utcnow())

    return user.save().serialize()

def find_user_by_id(user_id):
    found_user = User.query.get(user_id)
    if found_user is None:
        raise InvalidUsage.user_not_found()
    return found_user

