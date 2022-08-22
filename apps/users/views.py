from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from core.permissions.user_permissions import IsSuperUser

from .serializers import AddAvatarSerializer, UserSerializer

UserModel = get_user_model()


class UserListCreateView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = (AllowAny,)


class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()


class UserToDoctorView(GenericAPIView):
    permission_classes = (IsSuperUser,)
    queryset = UserModel.objects.all()

    def patch(self, *args, **kwargs):
        user = self.get_object()
        user.is_staff = True
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class DoctorToUserView(GenericAPIView):
    permission_classes = (IsSuperUser,)
    queryset = UserModel.objects.all()

    def patch(self, *args, **kwargs):
        user = self.get_object()
        user.is_staff = False
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class AddAvatarView(UpdateAPIView):
    serializer_class = AddAvatarSerializer

    def get_object(self):
        return self.request.user.profile




