from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    #                   null-> database-related  blank-> form validation-related
    age = models.PositiveIntegerField(null=True, blank=True)
# Create your models here.
