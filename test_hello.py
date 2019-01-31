from flask import abort
from myapp import app, mongo
from myapp.models import DBmanager
from myapp.commands import forge_data, initdb

import unittest

class TestCase(unittest.TestCase):

    def setUp(self):
        app.config.update(
            TESTING=True,
            WTF_CSRF_ENABLED=False,
            MONGO_DBNAME="testcase"
        )
        self.client = app.test_client()
        self.runner = app.test_cli_runner()

    def tearDown(self):
        mongo.delete_many({})
        mongo.drop()

    def test_app_exist(self):
        self.assertFalse(app is None)

    def test_app_is_testing(self):
        self.assertTrue(app.config['TESTING'])

    def test_404_page(self):
        response = self.client.get('/nothing')
        data = response.get_data(as_text=True)
        self.assertIn("404 Error", data)
        self.assertIn("Go Back", data)
        self.assertEqual(response.status_code, 404)

    def test_500_page(self):
        @app.route('/500')
        def internal_server_error_for_test():
            abort(500)

        response = self.client.get('/500')
        data = response.get_data(as_text=True)
        self.assertEqual(response.status_code, 500)
        self.assertIn('500 Error', data)
        self.assertIn('Go Back', data)

    def test_home_page(self):
        response = self.client.get('/')
        data = response.get_data(as_text=True)
        self.assertIn('hello', data)

    def test_create_message(self):
        response = self.client.post("/", data=dict(
            name="",body="hello world"
        ),follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertIn('This field is required.', data)

    def test_command_forge(self):
        result = self.runner.invoke(forge_data)
        self.assertIn('Add 20 fake messages.', result.output)
        # self.assertEqual(len(mongo.find({})), 20)

    def test_initdb_command_with_drop(self):
        result = self.runner.invoke(initdb, ['--drop'], input='y\n')
        self.assertIn('This operation will delete the database, do you want to continue?', result.output)
        self.assertIn('Data all clear.', result.output)


if __name__ == '__main__':
    unittest.main()
