import unittest

from fastapi.testclient import TestClient


class TestUser(unittest.TestCase):
    test_client: TestClient

    def setUp(self) -> None:
        from src.api.app import app

        self.test_client = TestClient(app)

    def test_read_root(self) -> None:
        response = self.test_client.get("/user/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Hello World"})


if __name__ == "__main__":
    unittest.main()
