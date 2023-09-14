from database import db

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column("product_id", db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(100))
    cost = db.Column(db.Double)
    img_url = db.Column(db.String(255))

    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    def __init__(self, name, description, cost, img_url, user_id):
        self.name = name
        self.description = description
        self.cost = cost
        self.img_url = img_url
        self.user_id = user_id

    def serialize(self):
        return {"id": self.id,
                "name": self.name,
                "description": self.description,
                "cost": self.cost,
                "img_url": self.img_url,
                "user_id": self.user_id}