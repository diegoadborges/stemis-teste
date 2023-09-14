from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):

    __tablename__ = 'users'
    id = db.Column("user_id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    money = db.Column(db.Double)


    def __init__(self, name):
        self.name = name
        self.money = 0

    def serialize(self):
        return {"id": self.id,
                "name": self.name,
                "money": self.money}
    
    def update(self, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        return self.save() or self

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def set_name(self, name):
        self.name = name