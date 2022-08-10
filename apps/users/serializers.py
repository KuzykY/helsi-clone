from rest_framework.serializers import ModelSerializer

from .models import ProfileModel, UserModel


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = ProfileModel


class UserSerializer(ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = UserModel
