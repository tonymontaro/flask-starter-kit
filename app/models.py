from werkzeug.security import generate_password_hash, check_password_hash

from app import db


class User(db.Model):
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

    def __repr__(self):
        """User representation"""
        return '<User {}>'.format(self.email)
