from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from user.serializers import UserSerializer, AuthTokenSerializer


class CreateUserView(generics.CreateAPIView):
    """ Create a new user """
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """ Create a new Auth Token for user """
    serializer_class = AuthTokenSerializer
    # Chapter-45 10:00
    # renderer_classes are added to make it usable from browser
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
