"""Sample API routes."""
from flask import Blueprint, jsonify
from flask_login import login_required

api_bp = Blueprint('api', __name__)


@api_bp.route('/', methods=['GET'])
def home():
    """Welcome page/message."""
    return jsonify({'message': 'Hello World!'})


@api_bp.route('/protected', methods=['GET'])
@login_required
def protected():
    """A protected route."""
    return jsonify({'message': 'You are logged-in.'})
