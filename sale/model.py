from database import db
import datetime as dt

class Sale(db.Model):
    __tablename__ = 'sales'
    id = db.Column("sale_id", db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)

    buyer_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'))

    def __init__(self, buyer_id, product_id):
        self.buyer_id = buyer_id
        self.product_id = product_id

    def serialize(self):
        return {"id": self.id,
                "buyer_id": self.buyer_id,
                "product_id": self.product_id,
                "created_at": self.created_at}