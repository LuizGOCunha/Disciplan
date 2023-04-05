import pytest

from website.models import User, Activity


@pytest.mark.django_db
class TestModels:
    def test_if_we_can_create_user_model(self, user_info):
        user = User(
            first_name=user_info["first_name"],
            last_name=user_info["last_name"],
            email=user_info["email"],
        )
        user.set_password(user_info["password"])
        user.full_clean()
        user.save()

        assert (
            User.objects.count() == 1
        ), "Number of user objects is not the correct amount"
        db_user = User.objects.first()
        assert (
            db_user.first_name == user.first_name
        ), "User from db doesn't have correct first name"
        assert (
            db_user.last_name == user.last_name
        ), "User from db doesn't have correct last name"
        assert db_user.email == user.email, "User from db doesn't have correct email"
        assert db_user.check_password(
            user_info["password"]
        ), "User from db doesn't have correct password"

    def test_if_we_can_create_an_activity_model(self, user_data, activity_info):
        activity = Activity(
            user=user_data["object"],
            title=activity_info["title"],
            description=activity_info["description"],
            difficulty=activity_info["difficulty"],
        )
        activity.full_clean()
        activity.save()

        assert (
            Activity.objects.count() == 1
        ), "Number of activity objects is not the correct amount"
        db_activity = Activity.objects.first()
        assert (
            db_activity.title == activity_info["title"]
        ), "Activity from db does not have correct title"
        assert (
            db_activity.description == activity_info["description"]
        ), "Activity from db does not have correct description"
        assert (
            db_activity.difficulty == activity_info["difficulty"]
        ), "Activity from db does not have correct difficulty"
