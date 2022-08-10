from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class UserModel(AbstractBaseUser):
    class Meta:
        db_table = 'users'


class ProfileModel(models.Model):
    class Meta:
        db_table = 'profile'
        first_name = models.CharField(max_length=20)
        last_name = models.CharField(max_length=40)
        phone_number = models.CharField(max_length=16)
        age = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)])
        user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')
        is_doctor = models.BooleanField(default=False)
        is_patient = models.BooleanField(default=True)


class PatientModel(models.Model):
    class Meta:
        db_table = 'patient'


class DoctorModel(models.Model):
    class Meta:
        db_table = 'doctor'
