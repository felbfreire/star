from httpx import Client
import pytest


url = 'http://localhost:8000'

class TestCli():

    def test_homepage_statuscodo_200(self):
        with Client(base_url=url) as client:
            status_code = client.get('/').status_code
            assert status_code == 200

    def test_homepage_method_post_should_return_405(self):
        with Client(base_url=url) as client:
            status_code = client.post('/').status_code
            assert status_code == 405

    def test_userpage_greets_user(self):
        with Client(base_url=url) as client:
            user = 'Alfred'
            content = client.get('/{}'.format(user)).content
            assert content == b'Hello Alfred'
