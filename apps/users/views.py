from rest_framework.generics import GenericAPIView, ListCreateAPIView, UpdateAPIView

from .models import UserModel
from .serializers import UserSerializer


class UserListCreateView(ListCreateAPIView):

    serializer_class = UserSerializer
    queryset = UserModel.objects.all()