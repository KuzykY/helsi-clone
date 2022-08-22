from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from core.permissions.user_permissions import IsStaff

from .models import MedicalCardModel
from .serializers import MedicalCardSerializers


class MedicalCardListCreateView(ListCreateAPIView):
    serializer_class = MedicalCardSerializers
    queryset = MedicalCardModel.objects.all()
    permission_classes =(IsAuthenticated,)

class MedicalCardRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    serializer_class = MedicalCardSerializers
    queryset = MedicalCardModel.objects.all()
    permission_classes = (IsStaff,)
