from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from core.services.jwt_service import JwtService


class ActivateUserView(GenericAPIView):
    def get(self, *args, **kwargs):
        token = kwargs.get('token')
        user = JwtService.validate_token(token)
        user.is_active = True
        user.save()
        return Response(status=status.HTTP_200_OK)
