import unittest
from unittest.mock import patch
import psycopg2
from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        app.app.config['TESTING'] = True
        app.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.app.test_client()

    def test_hello_world(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "<p>Hello, World!</p>")

    def test_create_city(self):
        city_data = [
            {
                "department_code": "75",
                "insee_code": "75056",
                "zip_code": "75001",
                "name": "Paris",
                "lat": 48.8566,
                "lon": 2.3522
            },
            {
                "department_code": "44",
                "insee_code": "44000",
                "zip_code": "44000",
                "name": "Nantes",
                "lat": 47.2184,
                "lon": -1.5536
            }
        ]

        response = self.app.post('/city', json=city_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {"message": "Cities added successfully"})

    def test_create_city_invalid_data(self):
        city_data = {
            "department_code": "75",
            "insee_code": "75056",
            "zip_code": "75001",
            "name": "Paris",
            "lat": 48.8566,
            "lon": 2.3522
        }

        response = self.app.post('/city', json=city_data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {"error": "Request body must be a list of objects"})

    def test_create_city_missing_fields(self):
        city_data = [
            {
                "department_code": "75",
                "insee_code": "75056",
                "zip_code": "75001",
                "name": "Paris",
                "lat": 48.8566
                # missing 'lon'
            }
        ]

        response = self.app.post('/city', json=city_data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {"error": "Missing fields in one of the records"})

    def test_city_get(self):
        # Assuming you have inserted some test data into the database
        # before running this test
        response = self.app.get('/city')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Paris", response.data.decode())
        self.assertIn("Nantes", response.data.decode())

    def test_health_check(self):
        response = self.app.get('/_health')
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()
