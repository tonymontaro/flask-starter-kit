from flask import request
from flask_restful import Resource
from flask_login import login_user, logout_user

from app.models import User


class Register(Resource):
    """Register User route."""
    def post(self):
        email = request.form.get('email')
        password = request.form.get('password')
        new_user = User.register(email, password)
        if new_user:
            return {'message': 'Registration successful.'}
        return {'message': 'Invalid username or password.'}


class Login(Resource):
    """Login User route."""
    def post(self):
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.get_user(email, password)
        if user:
            login_user(user)
            return {'message': 'Login successful.'}
        return {'message': 'Invalid username or password.'}


class Logout(Resource):
    """Logout User route."""
    def post(self):
        logout_user()
        return {'message': 'Logged out.'}
