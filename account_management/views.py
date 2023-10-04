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


class SignInViews(viewsets.ModelViewSet):
    def create(self, request, *args, **kwargs):
        try:
            user = authenticate(request.data.get('username', ''), request.data.get('password', ''))
            if user:
                token, _ = Token.objects.create(user=user)
                data = {"token": token,
                        'username': request.data.get('username', '')}
                return ok(data=data)
            else:
                return bad_request(data=[], message="Invalid credentials")

        except Exception as er:
            print(str(er))
            return internal_server_error(data=[])


class GroupViews(viewsets.ModelViewSet):
    def create(self, request, *args, **kwargs):
        try:
            serialized_data = GroupSerializer(data=request.data)
            if serialized_data.is_valid():
                serialized_data.save()
                return ok(data=serialized_data.data)
        except Exception as er:
            print(er)
            return internal_server_error(data=[])
