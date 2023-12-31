from flask import jsonify


def template(data, code=500):
    return {"message": {"errors": {"body": data}}, "status_code": code}


USER_NOT_FOUND = template(["User not found"], code=404)
PRODUCT_NOT_FOUND = template(["Product not found"], code=404)
INVALID_OPERATION = template(["Invalid operation"], code=400)
INSUFFICIENT_MONEY = template(["User has no money to buy this product"], code=400)
INSUFFICIENT_QUANTITY = template(["The product is not available"], code=400)
INVALID_VALUE = template(["Invalid value"], code=400)
USERNAME_EXISTS = template(["User already exists"], code=400)
DELETION_ERROR_USER = template(["You cannot delete this user as there is a related sale"], code=400)
DELETION_ERROR_PRODUCT = template(["You cannot delete this product as there is a related sale"], code=400)

UNKNOWN_ERROR = template([], code=500)


class InvalidUsage(Exception):
    status_code = 500

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_json(self):
        rv = self.message
        return jsonify(rv)

    @classmethod
    def user_not_found(cls):
        return cls(**USER_NOT_FOUND)

    @classmethod
    def product_not_found(cls):
        return cls(**PRODUCT_NOT_FOUND)

    @classmethod
    def insufficient_money(cls):
        return cls(**INSUFFICIENT_MONEY)

    @classmethod
    def insufficient_quantity(cls):
        return cls(**INSUFFICIENT_QUANTITY)

    @classmethod
    def invalid_operation(cls):
        return cls(**INVALID_OPERATION)

    @classmethod
    def unknown_error(cls):
        return cls(**UNKNOWN_ERROR)

    @classmethod
    def invalid_value(cls):
        return cls(**INVALID_VALUE)
    
    @classmethod
    def username_exists(cls):
        return cls(**USERNAME_EXISTS)
    
    @classmethod
    def deletion_error_user(cls):
        return cls(**DELETION_ERROR_USER)

    @classmethod
    def deletion_error_product(cls):
        return cls(**DELETION_ERROR_PRODUCT)



