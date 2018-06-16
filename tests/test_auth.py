"""Module for testing the user registration and login."""
import unittest
import json

from app import create_app, db
from tests.helpers import user1, get_json


class AuthTestCase(unittest.TestCase):
    """User authentication tests."""

    def setUp(self):
        """Setup test client."""
        self.app = create_app("testing")
        self.client = self.app.test_client()
        with self.app.app_context():
            db.session.close()
            db.drop_all()
            db.create_all()

    def test_user_registration(self):
        """Test for successful user registration."""
        res = self.client.post('/users/register', data=user1)
        result = get_json(res)
        self.assertEqual(result['message'], "Registration successful.")
        self.assertEqual(res.status_code, 201)

    def register(self):
        """Register user."""
        res = self.client.post('/users/register', data=user1)
        self.assertEqual(res.status_code, 201)

    def test_invalid_user_registration(self):
        """Test for registration when the user already exists."""
        self.register()
        res = self.client.post('/users/register', data=user1)
        self.assertEqual(res.status_code, 400)
        result = get_json(res)
        self.assertEqual(result['message'], "Invalid username or password.")

    def test_user_login(self):
        """Test for user login."""
        self.register()
        login_res = self.client.post('/users/login', data=user1)
        result = get_json(login_res)
        self.assertEqual(result['message'], "Login successful.")
        self.assertEqual(login_res.status_code, 200)

    def test_user_invalid_login(self):
        """Test for invalid user login."""
        self.register()
        wrong_pass_user = {
            'email': 'montaro@gmail.com',
            'password': 'wrong-password'
        }
        login_res = self.client.post('/users/login', data=wrong_pass_user)
        result = get_json(login_res)
        self.assertEqual(result['message'], "Invalid username or password.")
        self.assertEqual(login_res.status_code, 401)

    def login(self):
        """Login user."""
        self.register()
        login_res = self.client.post('/users/login', data=user1)
        self.assertEqual(login_res.status_code, 200)

    def test_login_required_for_protected_routes(self):
        """Test for route protection."""
        un_protected = get_json(self.client.get('/'))
        self.assertEqual(un_protected['message'], 'Hello World!')
        protected = self.client.get('/protected')
        self.assertEqual(protected.status_code, 401)

        self.login()
        protected = self.client.get('/protected')
        result = get_json(protected)
        self.assertEqual(protected.status_code, 200)
        self.assertEqual(result['message'], 'You are logged-in.')

    def test_user_logout(self):
        """Test for user login."""
        self.login()
        logout_res = self.client.post('/users/logout')
        result = get_json(logout_res)
        self.assertEqual(result['message'], 'Logged out.')
        self.assertEqual(logout_res.status_code, 200)

    def test_delete_user(self):
        """Test that a user can delete his/her account."""
        self.login()
        res = self.client.delete('/users', data=user1)
        result = get_json(res)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(result['message'], 'Your account has been deleted.')

    def test_only_authorized_user_can_delete_account(self):
        """Test that only a logged-in user can delete his/her account."""
        self.login()
        res = self.client.delete('/users')
        result = get_json(res)
        self.assertEqual(res.status_code, 403)
        self.assertEqual(result['message'], 'Unauthorized.')

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()


if __name__ == "__main__":
    unittest.main()
