"""Application models."""
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager


class DBHelper(object):
    """Perform common SQLAlchemy tasks."""

    @staticmethod
    def add(item):
        """Add item to database."""
        db.session.add(item)
        db.session.commit()

    @staticmethod
    def delete(item):
        """Delete an item from the database."""
        db.session.delete(item)
        db.session.commit()


class User(UserMixin, db.Model):
    """User model, used for registration and login."""

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def set_password(self, password):
        """Set user password hash."""
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """Verify user's password."""
        return check_password_hash(self.password, password)

    @staticmethod
    def register(email, password):
        """Register a user."""
        prev_user = User.query.filter_by(email=email).first()
        if email and password and not prev_user:
            user = User(email=email)
            user.set_password(password)
            DBHelper.add(user)
            return user
        return None

    @staticmethod
    def get_user(email, password):
        """Find and authenticate a user."""
        user = User.query.filter_by(email=email).first()
        if user and password and user.check_password(password):
            return user
        return None

    @staticmethod
    def get_by_id(id_, password):
        """Find a user by id."""
        user = User.query.get(id_)
        if user and password and user.check_password(password):
            return user
        return None

    def delete(self):
        """Delete a user's account"""
        return DBHelper.delete(self)


@login_manager.user_loader
def load_user(user_id):
    """User loader for Flask-Login."""
    return User.query.get(user_id)
