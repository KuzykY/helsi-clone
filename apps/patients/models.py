from django.contrib.auth import get_user_model
from django.db import models

# from apps.doctors.models import DoctorModel
from apps.medical_cards.models import MedicalCardModel
from apps.users.models import ProfileModel

UserModel = get_user_model()


class PatientModel(models.Model):
    class Meta:
        db_table = 'patients'

    profile = models.OneToOneField(ProfileModel, on_delete=models.CASCADE, blank=True)
    # doctors = models.ManyToManyField('DoctorModel', through='AppointmentModel',related_name='patients')
    medical_card = models.OneToOneField(MedicalCardModel, on_delete=models.CASCADE, blank=True)



# class AppointmentModel(models.Model):
#     class Meta:
#         db_table = 'appointment'
#
#     doctor = models.ForeignKey(DoctorModel, on_delete=models.CASCADE)
#     patient = models.ForeignKey(PatientModel, on_delete=models.CASCADE)
#     date = models.DateTimeField('Created Time', auto_now_add=True, blank=True)
#     is_accepted = models.BooleanField(default=None, blank=True)
