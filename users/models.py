import random

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from .tasks import task_send_mail_utils_password, task_send_sms_utils_password


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Must have email")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


def gen_utils_password(email, phone):
    password = ""
    for i in range(5):
        password += str(random.randint(0, 10))

    # if not phone is None:
    #     task_send_sms_utils_password.delay(password, phone)
    task_send_mail_utils_password.delay(password, email)
    return password


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=255, blank=True, null=True, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    phone = models.CharField(max_length=50, blank=True, null=True, unique=True, default=" ")
    utils_password = models.CharField(max_length=200, blank=True, null=True)
    is_created = models.BooleanField(default=False, blank=True, null=True)
    objects = UserManager()

    USERNAME_FIELD = "email"

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        if not self.is_created:
            self.utils_password = gen_utils_password(self.email, self.phone)
            self.is_created = True
        try:
            if self.phone:
                self.username = self.phone
                return super(User, self).save(*args, **kwargs)
        except TypeError:
            return super(User, self).save(*args, **kwargs)
