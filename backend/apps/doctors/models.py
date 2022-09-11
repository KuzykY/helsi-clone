from django.db import models

from apps.patients.models import PatientModel


class DoctorModel(models.Model):
    class Meta:
        db_table = 'doctors'
        ordering = ['id']

    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=40)
    speciality = models.CharField(max_length=200)
    patients = models.ManyToManyField(PatientModel, through='AppointmentModel')


class AppointmentModel(models.Model):
    class Meta:
        db_table = 'appointment'

    doctor = models.ForeignKey(DoctorModel, on_delete=models.CASCADE)
    patient = models.ForeignKey(PatientModel, on_delete=models.CASCADE)
    date = models.DateTimeField('Created Time', auto_now_add=True, blank=True)
    is_accepted = models.BooleanField(default=None, blank=True)
