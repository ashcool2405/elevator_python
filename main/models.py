from django.db import models
from django.utils import timezone
# import django
from django.conf import settings
from django.utils.timezone import activate
activate(settings.TIME_ZONE)
from django.contrib import admin
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy
class CustomAccountManager(BaseUserManager):
    def create_user(self, email, password, **other_fields):
        other_fields.setdefault("is_active", True)
        if not email:
            raise ValueError(gettext_lazy("You must provide an email"))
        email = self.normalize_email(email)
        user = self.model(email = email, **other_fields)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, email, password, **other_fields):
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_active", True)
        return self.create_user(email, password, **other_fields)
class NewUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(gettext_lazy("Email Address"), unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    username = models.CharField(max_length=150, blank=True, null=True)
    start_Date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    objects = CustomAccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.email
