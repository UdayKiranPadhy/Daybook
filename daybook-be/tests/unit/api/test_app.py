import unittest


class TestApp(unittest.TestCase):
    def test_app(self) -> None:
        from src.api.app import app

        self.assertIsNotNone(app)
        self.assertEqual(app.title, "ShieldMail API")
        self.assertEqual(app.openapi_version, "1.0.0")


if __name__ == "__main__":
    unittest.main()
