from rest_framework.serializers import ModelSerializer

from ..medical_cards.serializers import MedicalCardSerializers
from ..users.serializers import ProfileSerializer
from .models import PatientModel


class PatientSerializer(ModelSerializer):
    medical_card = MedicalCardSerializers(read_only=True)
    profile = ProfileSerializer()

    class Meta:
        model = PatientModel
        fields = ('id', 'profile', 'medical_card')

    def create(self, validated_data):
        return super().create(validated_data)
