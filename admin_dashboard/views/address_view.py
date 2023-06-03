from flask import Blueprint

from ..controllers.address_controller import list, insert, update, delete

address_bp = Blueprint('address_bp', __name__)

address_bp.route('/<string:client_id>', methods=['GET'])(list)
address_bp.route('/<string:client_id>', methods=['POST'])(insert)
address_bp.route('/<string:client_id>/<string:address_id>', methods=['PATCH'])(update)
address_bp.route('/<string:client_id>/<string:address_id>', methods=['DELETE'])(delete)
