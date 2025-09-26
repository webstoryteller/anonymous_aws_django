from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    nickname = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table="user"