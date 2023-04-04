import pytest

from django.test import Client, RequestFactory
from django.urls import reverse

from website.models import User, Activity


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

    def test_if_we_can_create_user_through_view(self, user_info):
        # Creates a password confirmation field so we can use it on this view
        user_info["password_c"] = user_info["password"]
        self.client.post(path=reverse("register"), data=user_info)
        number_of_users = User.objects.count()
        assert number_of_users == 1
        user = User.objects.first()
        assert user.first_name == user_info["first_name"]
        assert user.last_name == user_info["last_name"]
        assert user.email == user_info["email"]
        assert user.check_password(user_info["password"])

    def test_if_we_can_login_through_loginv_view(self, user_data):
        email = user_data["credentials"]["email"]
        password = user_data["credentials"]["password"]
        response = self.client.post(
            path=reverse("login"),
            data={
                "email": email,
                "password": password,
            },
        )

        assert response.status_code == 302
        assert self.client.session.session_key, "Failed to create Session"

    def test_if_we_can_logout_through_view(self, user_data):
        email = user_data["credentials"]["email"]
        password = user_data["credentials"]["password"]
        self.client.login(username=email, password=password)
        self.client.get(path=reverse("logout"))

        assert not self.client.session.session_key, "We still have a session key"

    def test_if_we_can_create_an_activity_object_through_activity_view(
        self, user_data, activity_info
    ):
        email = user_data["credentials"]["email"]
        password = user_data["credentials"]["password"]
        self.client.login(username=email, password=password)
        self.client.post(path=reverse("activities"), data=activity_info)

        assert Activity.objects.count() != 0, "No activities created in the database"
        activity = Activity.objects.first()
        assert (
            activity.user == user_data["object"]
        ), "Activity has no connection with the user that created it"
