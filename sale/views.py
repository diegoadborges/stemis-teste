from flask import Blueprint, request
from sale.model import Sale
import datetime as dt
from exceptions import InvalidUsage

blueprint = Blueprint('sale', __name__)

@blueprint.route('/api/sale', methods=(['GET']))
def get_sale():
    serializedSale = []

    for sale in Sale.query.all():
        serializedSale.append(sale.serialize())

    return serializedSale