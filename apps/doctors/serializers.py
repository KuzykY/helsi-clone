from rest_framework.serializers import ModelSerializer

from ..patients.serializers import PatientSerializer
from .models import DoctorModel


class DoctorSerializer(ModelSerializer):
    patients = PatientSerializer(many=True, read_only=True)

    class Meta:
        model = DoctorModel
        fields = ('id', 'name', 'surname', 'patients')

    def create(self, validated_data):
        return super().create(validated_data)
