from django.db import models


class DoctorModel(models.Model):
    class Meta:
        db_table = 'doctors'

    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=40)
    speciality = models.CharField(max_length=200)
