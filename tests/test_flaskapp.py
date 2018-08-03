import unittest,json

from main import app


class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_unauthorized(self):
        response = self.app.get('/authorized')
        # Check if the request fails with authorization error
        self.assertEqual(response._status_code,401,'Unauthorized access to page without login')

    def test_multiply(self):
        response = self.app.get('/multiply?x=5&y=7')
        resp = json.loads(response.data.decode('utf-8'))
        self.assertEqual(resp['answer'],35,'Multiply endpoint failed known answer 7*5 = 35')


    # TODO DEFINE TWO MORE TESTS ON THE END POINTS
    def test_touppercase(self):
        received = self.app.get('/touppercase?s=hello')
        response = json.loads(received.data.decode('utf-8'))
        self.assertEqual(response['answer'],'HELLO', 'test')

    def test_hello(self):
        received = self.app.get('/')
        response = json.loads(received.data.decode('utf-8'))
        self.assertEqual(response['answer'], 'Hello World!', 'test')

if __name__ == '__main__':
    unittest.main()
