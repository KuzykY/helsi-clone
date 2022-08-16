from django.contrib.auth import get_user_model
from django.db import models

from apps.doctors.models import DoctorModel
from apps.users.models import ProfileModel

UserModel = get_user_model()


class PatientModel(models.Model):
    class Meta:
        db_table = 'patients'

    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, blank=True)
    doctors = models.ManyToManyField(DoctorModel, through='Appointment')


class Appointment(models.Model):
    doctor = models.ForeignKey(DoctorModel, on_delete=models.CASCADE)
    patient = models.ForeignKey(PatientModel, on_delete=models.CASCADE)
