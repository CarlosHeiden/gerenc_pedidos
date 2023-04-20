from rest_framework import viewsets

from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

from django.contrib.auth import get_user_model
from .serializers import UserSerializer

from rest_framework.permissions import IsAuthenticated


class UserViewSet(viewsets.ModelViewSet):

    queryset = get_user_model().objects
    serializer_class = UserSerializer
    http_method_names = ['post']