from .model import Sale
from database import db
from sqlalchemy import text

def find_sale_by_buyer(id):
    return Sale.query.filter_by(buyer_id=id)

def find_sale_by_product(id):
    return Sale.query.filter_by(product_id=id)

def find_sale_by_seller(id):
    query = text(f"""SELECT u.* FROM sales s 
        INNER JOIN products p ON p.product_id = s.product_id
        INNER JOIN users u ON p.user_id = u.user_id WHERE u.user_id = {id};""")
    
    result = db.session.execute(query).first()

    return result