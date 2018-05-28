from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager


class User(UserMixin, db.Model):
    """User model, used for registration and login"""
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
        prev_user = User.query.filter_by(email=email).first()
        if email and password and not prev_user:
            user = User(email=email)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            return user
        return None

    @staticmethod
    def get_user(email, password):
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            return user
        return None

    def __repr__(self):
        """User representation"""
        return '<User {}>'.format(self.email)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
