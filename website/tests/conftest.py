import pytest

from website.models import User


@pytest.fixture()
def user_info() -> dict:
    data = {
        "first_name": "Nome",
        "last_name": "Sobrenome",
        "email": "test@email.com",
        "password": "123456",
    }
    return data


@pytest.fixture()
def user_data() -> dict:
    first_name = "Nome"
    last_name = "Sobrenome"
    email = "test@email.com"
    password = "123456"
    object = User(
        first_name=first_name,
        last_name=last_name,
        email=email,
    )
    object.set_password(password)
    object.full_clean()
    object.save()
    data = {"credentials": {"email": email, "password": password}, "object": object}
    return data
