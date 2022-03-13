import os
from functools import wraps

from flask import request, abort


APP_API_KEY = os.environ.get("APP_API_KEY")


def require_apikey(view_function):
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        if request.headers.get('x-api-key') and request.headers.get('x-api-key') == APP_API_KEY:
            return view_function(*args, **kwargs)
        else:
            abort(401)

    return decorated_function
