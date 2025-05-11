import unittest
from app import app

class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_registration(self):
        response = self.app.post('/register', data={'name': 'John', 'email': 'john@example.com'})
        self.assertEqual(response.status_code, 302)  # Redirect after POST

if __name__ == '__main__':
    unittest.main()