from functools import wraps
from flask import current_app, request, jsonify
import jwt

from .models.user import User

def authenticate(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message' : 'Token not found.'}), 400
  
        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
            user = User.get_by_field("id", data.get("id"))
            if not user.is_admin:
                return jsonify({
                'message' : 'The user does not have permission to do this action.'
            }), 403
        except Exception as E:
            print(E)
            return jsonify({
                'message' : 'Could not verify token.'
            }), 403
        
        return  f(*args, **kwargs)
  
    return decorated