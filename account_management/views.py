from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

from .serializers import *
from utils.response import *


class SignUpViews(viewsets.ModelViewSet):
    def create(self, request, *args, **kwargs):
        serialized_data = UserSerializer(data=request.data)
        if serialized_data.is_valid():
            instance = serialized_data.save()
            instance.is_active = False
            instance.save()
            return ok(data=serialized_data.data)


