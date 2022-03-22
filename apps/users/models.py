from django.db import models

from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import (
    AbstractUser,
    PermissionsMixin,
)

from .managers import CustomAccountManager


class NewUser(AbstractUser, PermissionsMixin):

    username = None
    email = models.EmailField("email address", unique=True)
    first_name = models.CharField("first name", max_length=150)
    last_name = models.CharField("last name", max_length=150)

    objects = CustomAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
