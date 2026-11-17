
import unittest

from app import app


class VisionAssistTests(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_homepage_loads(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)

        self.assertIn(
            b"VisionAssist AI",
            response.data
        )

    def test_health_endpoint(self):
        response = self.client.get("/health")

        self.assertEqual(response.status_code, 200)

        data = response.get_json()

        self.assertEqual(data["status"], "healthy")

        self.assertEqual(
            data["application"],
            "VisionAssist AI"
        )

    def test_about_endpoint(self):
        response = self.client.get("/about")

        self.assertEqual(response.status_code, 200)

        data = response.get_json()

        self.assertEqual(
            data["name"],
            "VisionAssist AI"
        )


if __name__ == "__main__":
    unittest.main()
