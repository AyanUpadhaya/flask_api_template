# utils/response.py
from flask import jsonify

def success_response(data=None, message="Success", status_code=200):
    return jsonify({
        "status": "success",
        "message": message,
        "data": data
    }), status_code

"""
usage:
return success_response(user_schema.dump(user))
"""