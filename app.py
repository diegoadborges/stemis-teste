from flask import Flask
from user.views import blueprint as user_blueprint
from product.views import blueprint as product_blueprint
from sale.views import blueprint as sale_blueprint
from database import db
from exceptions import InvalidUsage

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///shop.sqlite3"

def errorhandler(error):
        response = error.to_json()
        response.status_code = error.status_code
        return response

if __name__ == "__main__":
    app.app_context().push()
    app.debug = True
    db.init_app(app)
    db.create_all()

    app.errorhandler(InvalidUsage)(errorhandler)
    
    app.register_blueprint(user_blueprint)
    app.register_blueprint(product_blueprint)
    app.register_blueprint(sale_blueprint)
    app.run()

