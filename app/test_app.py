import unittest
from unittest.mock import patch
import psycopg2
from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_hello_world(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "Hello, World!")

    def test_create_city(self):
        response = self.app.post('/city', json={"name": "New York"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "City created successfully")

    def test_city_get(self):
        response = self.app.get('/city')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "List of cities")

    @patch('app.get_db_connection')
    def test_health_check(self, mock_get_db_connection):
        mock_get_db_connection.return_value = True
        response = self.app.get('/_health')
        self.assertEqual(response.status_code, 204)

    @patch('app.get_db_connection')
    def test_health_check_db_error(self, mock_get_db_connection):
        mock_get_db_connection.side_effect = psycopg2.Error
        response = self.app.get('/_health')
        self.assertEqual(response.status_code, 500)

if __name__ == '__main__':
    unittest.main()
