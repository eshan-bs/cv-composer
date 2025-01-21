from django.contrib.auth.models import User, AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    user_type = models.IntegerField(default=0)

    def __str__(self):
        return self.username
