from flask import Blueprint, request
from sale.model import Sale
from exceptions import InvalidUsage
from product.views import find_product_by_id
from user.views import find_user_by_id

blueprint = Blueprint('sale', __name__)

@blueprint.route('/api/sale', methods=(['GET']))
def get_sale():
    serializedSale = []

    for sale in Sale.query.all():
        serializedSale.append(sale.serialize())

    return serializedSale

@blueprint.route('/api/sale', methods=(['POST']))
def new_sale():
    buyer_id = request.json["buyer_id"]
    product_id = request.json["product_id"]

    product = find_product_by_id(product_id)
    buyer = find_user_by_id(buyer_id)
    seller = find_user_by_id(product.get_user_id())

    product_cost = product.get_cost()

    if buyer_id == product.get_user_id():
        raise InvalidUsage.invalid_operation()

    if product.get_quantity() <= 0:
        raise InvalidUsage.insufficient_quantity()

    if buyer.get_money() < product_cost:
        raise InvalidUsage.insufficient_money()
    
    buyer.discount_money(product_cost)
    seller.add_money(product_cost)
    product.decrease_quantity(1)

    seller.save(False)
    buyer.save(False)
    product.save(False)

    sale = Sale(buyer_id, product_id, product_cost).save()

    return sale.serialize()