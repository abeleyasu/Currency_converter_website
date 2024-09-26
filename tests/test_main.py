import unittest
from app import create_app

class MainTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.config['TESTING'] = True

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Welcome to the Portfolio Project', response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()

