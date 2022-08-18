from django.db import models


class MedicalCardModel(models.Model):
    class Meta:
        db_table = 'medical_cards'

    blood_type = models.CharField(max_length=2)
    symptoms = models.CharField(max_length=150)
    medication = models.CharField(max_length=255)
