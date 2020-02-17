from django.test import TestCase


class TestRandomView(TestCase):
    def test_request(self):
        response = self.client.get('/random')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["status"], "ok")
        self.assertIsInstance(response.data["number"], int)
        self.assertGreaterEqual(response.data["number"], 1)
        self.assertLessEqual(response.data["number"], 100)
