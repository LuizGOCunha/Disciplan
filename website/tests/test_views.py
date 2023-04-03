import pytest

from django.test import Client, RequestFactory
from django.urls import reverse

from website.models import User


@pytest.mark.django_db
class TestViews:
    client = Client()
    factory = RequestFactory()

    def test_status_code_of_views_while_logged(self, user_data):
        email = user_data["credentials"]["email"]
        password = user_data["credentials"]["password"]
        bol = self.client.login(
            username=email,
            password=password,
        )
        view_names_200 = [
            "index",
            "register",
            "login",
            "activities",
        ]
        view_names_302 = [
            "logout",
        ]
        # Test views that should return 200
        for name in view_names_200:
            response = self.client.get(reverse(name))
            status_code = response.status_code
            assert (
                status_code == 200
            ), f"View '{name}' returned inadequate status code {status_code} instead of 200"
        # Test views that should return 302
        for name in view_names_302:
            response = self.client.get(reverse(name))
            status_code = response.status_code
            assert (
                status_code == 302
            ), f"View '{name}' returned status code {status_code} instead of redirecting with code 302"
