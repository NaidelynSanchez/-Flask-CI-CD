import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_home_status(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_content(self):
        response = self.client.get('/')
        print(response.data)  # 👈 para verificar
        self.assertIn(b'Hola', response.data)

if __name__ == '__main__':
    unittest.main()