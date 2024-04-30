import unittest
from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_city_get(self):
        response = self.app.get('/city')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'["Paris", "London", "New York"]')
    
    def test_health_check(self):
        response = self.app.get('/_health')
        self.assertEqual(response.status_code, 204)

    def test_hello_world(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'<p>Hello, World!</p>')
    




if __name__ == '__main__':
    unittest.main()