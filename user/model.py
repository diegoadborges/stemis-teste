from database import db
import datetime as dt

class User(db.Model):

    __tablename__ = 'users'
    id = db.Column("user_id", db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    money = db.Column(db.Double)
    created_at = db.Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)

    product = db.relationship('Product', cascade="all,delete", backref='users')

    def __init__(self, name):
        self.name = name
        self.money = 0

    def serialize(self):
        return {"id": self.id,
                "name": self.name,
                "money": self.money,
                "created_at": self.created_at,
                "updated_at": self.updated_at}

    def add_money(self, quantity):
        self.money += quantity

    def discount_money(self, quantity):
        self.money -= quantity

    def set_name(self, name):
        self.name = name

    def get_money(self):
        return self.money

    def get_created_at(self):
        return self.created_at

    def set_created_at(self, created_at):
        self.created_at = created_at

    def get_updated_at(self):
        return self.updated_at

    def set_updated_at(self, updated_at):
        self.updated_at = updated_at