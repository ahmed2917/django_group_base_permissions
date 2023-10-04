from rest_framework import viewsets
from django.contrib.auth import authenticate

from .serializers import *
from utils.response import *


class SignUpViews(viewsets.ModelViewSet):
    def create(self, request, *args, **kwargs):
        serialized_data = UserSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return ok(serialized_data.data)
