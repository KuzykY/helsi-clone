from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import MedicalCardModel
from .serializers import MedicalCardSerializers


class MedicalCardListCreateView(ListCreateAPIView):
    serializer_class = MedicalCardSerializers
    queryset = MedicalCardModel.objects.all()
