from flask import Blueprint, request
from product.model import Product


blueprint = Blueprint('product', __name__)

@blueprint.route('/api/product', methods=(['GET']))
def get_products():
    serializedProducts = []

    for product in Product.query.all():
        serializedProducts.append(product.serialize())

    return serializedProducts