from flask_sqlalchemy import SQLAlchemy
from database import db

class User(db.Model):

    __tablename__ = 'users'
    id = db.Column("user_id", db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    money = db.Column(db.Double)


    def __init__(self, name):
        self.name = name
        self.money = 0

    def serialize(self):
        return {"id": self.id,
                "name": self.name,
                "money": self.money}

    def add_money(self, quantity):
        self.money += quantity
        self.save()

    def set_name(self, name):
        self.name = name