from rest_framework import viewsets

from .serializers import *
from utils.response import *


class UserViews(viewsets.ModelViewSet):
    def create(self, request, *args, **kwargs):
        serialized_data = UserSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return ok(serialized_data.data)
