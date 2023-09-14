from flask import Flask
from user.views import blueprint as user_blueprint
from product.views import blueprint as product_blueprint
from flask_sqlalchemy import SQLAlchemy
from database import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///shop.sqlite3"

if __name__ == "__main__":
    app.app_context().push()
    app.debug = True
    db.init_app(app)
    db.create_all()

    app.register_blueprint(user_blueprint)
    app.register_blueprint(product_blueprint)
    app.run()