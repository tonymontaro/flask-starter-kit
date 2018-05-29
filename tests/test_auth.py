"""Module for testing the user registration and login."""
import unittest
import json

from app import create_app, db


class AuthTestCase(unittest.TestCase):
    """User authentication tests."""

    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.user_data = {
            'email': 'montaro@gmail.com',
            'password': 'password'
        }
        with self.app.app_context():
            db.session.close()
            db.drop_all()
            db.create_all()

    def test_user_registration(self):
        """Test for successful user registration."""
        res = self.client.post('/register', data=self.user_data)
        result = json.loads(res.data.decode())
        self.assertEqual(result['message'], "Registration successful.")
        self.assertEqual(res.status_code, 201)

    def test_registered_already(self):
        """Test for registration when the user already exists."""
        res = self.client.post('/register', data=self.user_data)
        self.assertEqual(res.status_code, 201)
        second_res = self.client.post('/register', data=self.user_data)
        self.assertEqual(second_res.status_code, 400)
        result = json.loads(second_res.data.decode())
        self.assertEqual(result['message'], "Invalid username or password.")

    def test_user_login(self):
        """Test for user login."""
        res = self.client.post('/register', data=self.user_data)
        self.assertEqual(res.status_code, 201)
        login_res = self.client.post('/login', data=self.user_data)
        result = json.loads(login_res.data)
        self.assertEqual(result['message'], "Login successful.")
        self.assertEqual(login_res.status_code, 200)

    def test_user_invalid_loginself(self):
        """Test for invalid user login."""
        res = self.client.post('/register', data=self.user_data)
        self.assertEqual(res.status_code, 201)
        wrong_pass_user = {
            'email': 'montaro@gmail.com',
            'password': 'wrong-password'
        }
        login_res = self.client.post('/login', data=wrong_pass_user)
        result = json.loads(login_res.data)
        self.assertEqual(result['message'], "Invalid username or password.")
        self.assertEqual(login_res.status_code, 401)

    def test_user_logout(self):
        """Test for user login."""
        res = self.client.post('/register', data=self.user_data)
        self.assertEqual(res.status_code, 201)
        login_res = self.client.post('/login', data=self.user_data)
        result = json.loads(login_res.data)
        self.assertEqual(login_res.status_code, 200)
        logout_res = self.client.post('/logout')
        result = json.loads(logout_res.data)
        self.assertEqual(result['message'], 'Logged out.')
        self.assertEqual(logout_res.status_code, 200)

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()


if __name__ == "__main__":
    unittest.main()
