from flask import Blueprint

from ..controllers.client_controller import list, insert, update, delete

client_bp = Blueprint('client_bp', __name__)

# route controllers here
client_bp.route('/', methods=['GET'])(list)
client_bp.route('/', methods=['POST'])(insert)
client_bp.route('/<string:client_id>', methods=['PATCH'])(update)
client_bp.route('/<string:client_id>', methods=['DELETE'])(delete)
