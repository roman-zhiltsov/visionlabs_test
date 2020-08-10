import base64
import json
import unittest

from api import app


class TestFlaskApi(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def get_response(self, line):
        response = self.app.get(line)
        return response.status_code, response.json


class TestImagesApi(TestFlaskApi):

    def test_all_methods(self):
        encoded_image = b'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'
        response = self.app.post('/image', data=encoded_image)
        answer_post = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('file_name', answer_post)
        self.assertIn('file_size', answer_post)
        self.assertIn('last_access', answer_post)

        file_name = answer_post['file_name']

        response = self.app.get('/image')
        answer_get = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(answer_post, answer_get)

        response = self.app.get(''.join(('/images/', file_name)))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(base64.b64encode(response.data), encoded_image)

        response = self.app.delete('/image', data=file_name)
        self.assertEqual(response.status_code, 200)
        self.assertEqual('ok', response.data.decode())

        response = self.app.get('/image')
        answer_get = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(answer_post, answer_get)


if __name__ == '__main__':
    unittest.main()
