import unittest
from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_city_get(self):
        response = self.app.get('/city')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(response.get_json(), ["Paris", "London", "New York"])

if __name__ == '__main__':
    unittest.main()