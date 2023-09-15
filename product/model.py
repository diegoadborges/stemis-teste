from database import db
import datetime as dt

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column("product_id", db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(100))
    cost = db.Column(db.Double)
    quantity = db.Column(db.Integer)
    img_url = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    def __init__(self, name, description, cost, quantity, img_url, user_id):
        self.name = name
        self.description = description
        self.cost = cost
        self.quantity = quantity
        self.img_url = img_url
        self.user_id = user_id

    def serialize(self):
        return {"id": self.id,
                "name": self.name,
                "description": self.description,
                "cost": self.cost,
                "quantity": self.quantity,
                "img_url": self.img_url,
                "user_id": self.user_id,
                "created_at": self.created_at,
                "updated_at": self.updated_at}
    
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_cost(self):
        return self.cost

    def set_cost(self, cost):
        self.cost = cost

    def get_quantity(self):
        return self.quantity
    
    def set_quantity(self, quantity):
        self.quantity = quantity

    def get_img_url(self):
        return self.img_url

    def set_img_url(self, img_url):
        self.img_url = img_url

    def get_user_id(self):
        return self.user_id

    def set_user_id(self, user_id):
        self.user_id = user_id

    def get_created_at(self):
        return self.created_at

    def set_created_at(self, created_at):
        self.created_at = created_at

    def get_updated_at(self):
        return self.updated_at

    def set_updated_at(self, updated_at):
        self.updated_at = updated_at