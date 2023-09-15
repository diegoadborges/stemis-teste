from flask import Blueprint, request
from product.model import Product
from user.views import find_user_by_id
import datetime as dt
from exceptions import InvalidUsage
from flasgger.utils import swag_from

blueprint = Blueprint('product', __name__)

@swag_from("../docs/product/list_products.yaml")
@blueprint.route('/api/product', methods=(['GET']))
def get_products():
    serializedProducts = []

    for product in Product.query.all():
        serializedProducts.append(product.serialize())

    return serializedProducts

@swag_from("../docs/product/create_product.yaml")
@blueprint.route('/api/product', methods=(['POST']))
def create_product():
    name = request.json["name"]
    description = request.json["description"]
    cost = request.json["cost"]
    quantity = request.json["quantity"]
    img_url = request.json["img_url"]
    user_id = request.json["user_id"]

    if cost <= 0 or quantity <= 0:
        raise InvalidUsage.invalid_operation()

    find_user_by_id(user_id)
    
    product = Product(name, description, cost, quantity, img_url, user_id)    

    return product.save().serialize()

@blueprint.route('/api/product/update', methods=(['PUT']))
def update_product():
    id = request.json["id"]
    name = request.json["name"]
    description = request.json["description"]
    cost = request.json["cost"]
    img_url = request.json["img_url"]
    quantity = request.json["quantity"]

    product = find_product_by_id(id)
    product.set_name(name)
    product.set_description(description)
    product.set_cost(cost)
    product.set_quantity(quantity)
    product.set_img_url(img_url)
    product.set_updated_at(dt.datetime.utcnow())

    return product.save().serialize()

@blueprint.route('/api/product/<int:id>', methods=(['DELETE']))
def delete_product(id):
    product = find_product_by_id(id)

    product.delete()
    return '', 200

def find_product_by_id(id):
    found_product = Product.query.get(id)
    if found_product is None:
        raise InvalidUsage.product_not_found()
    return found_product
