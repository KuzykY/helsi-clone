from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.db import models

from .enums import RegEx
from .managers import UserManager
from .services import upload_to


class UserModel(AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table = 'auth_user'

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255, validators=[
        RegexValidator(RegEx.PASSWORD.pattern, RegEx.PASSWORD.msg)
    ])
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)  # True - є лікарем
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'

    objects = UserManager()


class ProfileModel(models.Model):
    class Meta:
        db_table = 'profile'

    name = models.CharField(max_length=100, validators=[RegexValidator(RegEx.NAME.pattern, RegEx.NAME.msg)])
    surname = models.CharField(max_length=100, validators=[RegexValidator(RegEx.NAME.pattern, RegEx.NAME.msg)])
    phone_number = models.CharField(max_length=10, validators=[RegexValidator(RegEx.PHONE.pattern, RegEx.PHONE.msg)])
    age = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    avatar = models.ImageField(upload_to=upload_to, blank=True)
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')
    # patients=models.OneToOneField()
    # is_doctor = models.BooleanField(default=False)
    # is_patient = models.BooleanField(default=True)
