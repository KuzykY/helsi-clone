from rest_framework.serializers import ModelSerializer

from .models import MedicalCardModel


class MedicalCardSerializers(ModelSerializer):
    class Meta:
        model = MedicalCardModel
        fields = ('blood_type', 'symptoms', 'medication')
