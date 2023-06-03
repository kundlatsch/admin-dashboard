from flask import Blueprint

from ..controllers.user_controller import insert, login

user_bp = Blueprint('user_bp', __name__)

# route controllers here
user_bp.route('/', methods=['POST'])(insert)
user_bp.route('/login', methods=['POST'])(login)

