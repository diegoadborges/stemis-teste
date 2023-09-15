from flask import Blueprint, request
from product.model import Product
from user.views import find_user_by_id
import datetime as dt

blueprint = Blueprint('product', __name__)

@blueprint.route('/api/product', methods=(['GET']))
def get_products():
    serializedProducts = []

    for product in Product.query.all():
        serializedProducts.append(product.serialize())

    return serializedProducts

@blueprint.route('/api/product', methods=(['POST']))
def create_product():
    name = request.json["name"]
    description = request.json["description"]
    cost = request.json["cost"]
    img_url = request.json["img_url"]
    user_id = request.json["user_id"]
    
    find_user_by_id(user_id)
    
    product = Product(name, description, cost, img_url, user_id)    

    return product.save().serialize()

@blueprint.route('/api/product/update', methods=(['PUT']))
def update_product():
    id = request.json["id"]
    name = request.json["name"]
    description = request.json["description"]
    cost = request.json["cost"]
    img_url = request.json["img_url"]

    product = find_product_by_id(id)
    product.set_name(name)
    product.set_description(description)
    product.set_cost(cost)
    product.set_img_url(img_url)
    product.set_updated_at(dt.datetime.utcnow())

    return product.save().serialize()

def find_product_by_id(id):
    found_product = Product.query.get(id)
    if found_product is None:
        print("not found")
        # TODO create exception when user is not found
        return 
    return found_product