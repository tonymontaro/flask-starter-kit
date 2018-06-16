"""Authentication routes."""
from flask import request, Blueprint, jsonify
from flask_login import login_user, logout_user, current_user, login_required

from app.models import User


auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/register', methods=['POST'], strict_slashes=False)
def register():
    """Register User."""
    email = request.form.get('email')
    password = request.form.get('password')
    new_user = User.register(email, password)
    if new_user:
        return jsonify({'message': 'Registration successful.'}), 201
    return jsonify({'message': 'Invalid username or password.'}), 400


@auth_bp.route('/login', methods=['POST'], strict_slashes=False)
def login():
    """Login User."""
    email = request.form.get('email')
    password = request.form.get('password')
    user = User.get_user(email, password)
    if user:
        login_user(user)
        return jsonify({'message': 'Login successful.'}), 200
    return jsonify({'message': 'Invalid username or password.'}), 401


@auth_bp.route('/logout', methods=['POST'], strict_slashes=False)
def logout():
    """Logout User."""
    logout_user()
    return jsonify({'message': 'Logged out.'})


@auth_bp.route('', methods=['DELETE'])
@login_required
def delete_account():
    """Delete logged-in User's account."""
    password = request.form.get('password')
    user = User.get_by_id(current_user.id, password)
    if not user:
        return jsonify({'message': 'Unauthorized.'}), 403
    user.delete()
    return jsonify({'message': 'Your account has been deleted.'}), 200
