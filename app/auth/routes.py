"""Authentication routes."""
from flask import request
from flask_restful import Resource
from flask_login import login_user, logout_user

from app.models import User


class Register(Resource):
    """Register User resource."""

    def post(self):
        """Register User route."""
        email = request.form.get('email')
        password = request.form.get('password')
        new_user = User.register(email, password)
        if new_user:
            return {'message': 'Registration successful.'}, 201
        return {'message': 'Invalid username or password.'}, 400


class Login(Resource):
    """Login User resource."""

    def post(self):
        """Login User route."""
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.get_user(email, password)
        if user:
            login_user(user)
            return {'message': 'Login successful.'}, 200
        return {'message': 'Invalid username or password.'}, 401


class Logout(Resource):
    """Logout User resource."""

    def post(self):
        """Logout User route."""
        logout_user()
        return {'message': 'Logged out.'}
