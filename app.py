from flask import Flask
from user.views import blueprint as user_blueprint
from product.views import blueprint as product_blueprint
from sale.views import blueprint as sale_blueprint
from database import db
from exceptions import InvalidUsage
from flasgger import Swagger
from os import environ
from sqlalchemy import create_engine

app = Flask(__name__)
engine = create_engine(environ["DATABASE_URL"])

def errorhandler(error):
        response = error.to_json()
        response.status_code = error.status_code
        return response

app.app_context().push()
db.init_app(app)
db.create_all()

app.errorhandler(InvalidUsage)(errorhandler)
swagger = Swagger(app)
app.register_blueprint(user_blueprint)
app.register_blueprint(product_blueprint)
app.register_blueprint(sale_blueprint)

if __name__ == "__main__":
    app.run()