import unittest
from app.models import User, db

class UserModelTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_user_creation(self):
        with self.app.app_context():
            user = User(username='testuser', email='test@example.com', password='password')
            db.session.add(user)
            db.session.commit()

            queried_user = User.query.filter_by(username='testuser').first()
            self.assertIsNotNone(queried_user)
            self.assertEqual(queried_user.email, 'test@example.com')

if __name__ == '__main__':
    unittest.main()

