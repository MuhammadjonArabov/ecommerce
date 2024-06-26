import random

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from common.base import BaseModel
from common.manager import CustomUserManager
from common.validators import phone_number_validator


class Gender(models.IntegerChoices):
    MALE = 1, _('Male')
    FEMALE = 2, _('Female')


class UserRole(models.IntegerChoices):
    ADMIN = 1, _('Admin')
    CLIENT = 2, _('Client')
    MANAGER = 3, _('Manager')


class User(AbstractUser, BaseModel):
    last_name = None
    first_name = None
    email = None
    username = None
    name = models.CharField(_('Name of User'), max_length=255)
    phone = models.CharField(_('Phone number'), max_length=14, unique=True, null=True, blank=True,
                             validators=[phone_number_validator()])
    birthday = models.DateTimeField(_('Birthday'), null=True, blank=True, default=timezone.now)
    photo = models.ImageField(_('Photo of User'), upload_to='userImages', null=True, blank=True)
    role = models.PositiveIntegerField(choices=UserRole.choices, default=UserRole.CLIENT)
    gender = models.PositiveIntegerField(choices=Gender.choices, default=Gender.MALE)

    objects = CustomUserManager()

    EMAIL_FIELD = None
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name


class Code(BaseModel):
    user = models.ForeignKey(User, related_name='userCode', on_delete=models.CASCADE, null=True, blank=True)
    code = models.CharField(max_length=6, null=True, blank=True)

    def __str__(self):
        return self.code

    def generate_code(self):
        number = str(random.randint(100000, 999999))
        self.code = number
        self.save()
        return self.code
