from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import DoctorModel
from .serializers import DoctorSerializer


class DoctorListCreateView(ListCreateAPIView):
    serializer_class = DoctorSerializer
    queryset = DoctorModel.objects.all()


class DoctorRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    serializer_class = DoctorSerializer
    queryset = DoctorModel.objects.all()
