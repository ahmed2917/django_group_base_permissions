from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

from .serializers import *
from utils.response import *
from utils.common_functions import *


class SignUpViews(viewsets.ModelViewSet):
    def create(self, request, *args, **kwargs):
        try:
            serialized_data = UserSerializer(data=request.data)
            if serialized_data.is_valid():
                instance = serialized_data.save()
                instance.is_active = False
                instance.save()
                return ok(data=serialized_data.data)
            else:
                bad_request_msg = get_first_error_message_from_serializer_errors(serialized_data.errors,
                                                                                 'Bad request')
                return bad_request(data=[], message=bad_request_msg)
        except Exception as er:
            print(str(er))
            return internal_server_error(data=[])
