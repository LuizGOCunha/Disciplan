from django.db import models
from django.contrib.auth.models import AbstractBaseUser


# Create your models here.

class UserManager(models.Manager):
    def get_by_natural_key(self, email):
        return self.get(email=email)


class User(AbstractBaseUser):
    first_name = models.CharField(
        "First Name",
        max_length=100,
    )
    last_name = models.CharField("Second Name", max_length=100)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"

    objects = UserManager()

    def __str__(self) -> str:
        return f"{self.first_name} | {self.email}"


class Activity(models.Model):
    DIFFICULTY_CHOICES = (
        (100, "very easy"),
        (200, "easy"),
        (300, "medium"),
        (400, "hard"),
        (500, "very hard"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    difficulty = models.IntegerField(choices=DIFFICULTY_CHOICES)

    def __str__(self) -> str:
        return self.title
