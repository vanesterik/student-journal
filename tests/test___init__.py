import unittest

from flask import Flask

from app import create_app


class TestCreateApp(unittest.TestCase):
    def test_create_app(self):
        app = create_app()
        self.assertIsInstance(app, Flask)


if __name__ == "__main__":
    unittest.main()
