from flask import Blueprint, request
from product.model import Product
from user.views import find_user_by_id

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