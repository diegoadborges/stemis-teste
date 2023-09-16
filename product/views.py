from flask import Blueprint, request
from product.model import Product
from user.views import find_user_by_id
import datetime as dt
from exceptions import InvalidUsage
from flasgger.utils import swag_from
from sale.service import find_sale_by_product

blueprint = Blueprint('product', __name__)

@swag_from("../docs/product/list_products.yaml")
@blueprint.route('/api/product', methods=(['GET']))
def get_products():
    page = request.args.get("page")
    per_page = request.args.get("per_page")
    if page is None:
        page = 1
    if per_page is None:
        per_page = 5

    serializedProducts = []
    try:
        per_page = int(per_page)
        page = int(page)
        for product in Product.query.paginate(per_page=per_page, page=page):
            serializedProducts.append(product.serialize())
    except:
        InvalidUsage.invalid_value()

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

@swag_from("../docs/product/update_product.yaml")
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

@swag_from("../docs/product/delete_product.yaml")
@blueprint.route('/api/product/<int:id>', methods=(['DELETE']))
def delete_product(id):
    if find_sale_by_product(id).first() is not None:
        raise InvalidUsage.deletion_error_product()
    
    product = find_product_by_id(id)

    product.delete()
    return '', 200

@swag_from("../docs/product/find_by_id_product.yaml")
@blueprint.route('/api/product/<int:id>', methods=(['GET']))
def find_product_by_id(id):
    found_product = Product.query.get(id)
    if found_product is None:
        raise InvalidUsage.product_not_found()
    
    if request.method == "GET":
        return found_product.serialize()
    return found_product