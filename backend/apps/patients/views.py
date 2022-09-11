from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.patients.models import PatientModel
from apps.patients.serializers import PatientSerializer


class PatientListCreateView(ListCreateAPIView):
    serializer_class = PatientSerializer
    queryset = PatientModel.objects.all()


class PatientRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = PatientSerializer
    queryset = PatientModel.objects.all()
