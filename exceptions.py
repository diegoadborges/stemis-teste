from flask import jsonify

def template(data, code=500):
    return {'message': {'errors': {'body': data}}, 'status_code': code}


USER_NOT_FOUND = template(['User not found'], code=404)
PRODUCT_NOT_FOUND = template(['Product not found'], code=404)
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
    def unknown_error(cls):
        return cls(**UNKNOWN_ERROR)