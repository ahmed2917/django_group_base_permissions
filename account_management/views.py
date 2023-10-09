from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
# from django.contrib.auth.models import Permission

from .serializers import *
from utils.response import *
from utils.common_functions import *


class SignUpViews(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        try:
            serialized_data = UserSerializer(data=request.data)
            if serialized_data.is_valid():
                instance = serialized_data.save()
                instance.is_active = False
                instance.save()
                instance.set_password(instance.password)
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
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        try:
            user = authenticate(username=request.data.get('username', ''), password=request.data.get('password', ''))
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                data = {"token": str(token),
                        'username': request.data.get('username', '')}
                return ok(data=data)
            else:
                return bad_request(data=[], message="Invalid credentials")

        except Exception as er:
            print(str(er))
            return internal_server_error(data=[])


class UserViews(viewsets.ModelViewSet):
    def create(self, request, *args, **kwargs):
        try:
            serialized_data = UserSerializer(data=request.data)
            if serialized_data.is_valid():
                instance = serialized_data.save()
                instance.set_password(instance.password)
                instance.save()
                return ok(data=serialized_data.data)
        except Exception as er:
            print(str(er))
            return internal_server_error(data=[])

    def list(self, request, *args, **kwargs):
        try:
            queryset = User.objects.all()
            serialized_data = UserSerializer(queryset, many=True)
            if serialized_data:
                return ok(data=serialized_data.data)
            else:
                return ok(data=[])
        except Exception as er:
            print(str(er))
            return internal_server_error(data=[])

    def update(self, request, *args, **kwargs):
        try:
            user_queryset = User.objects.filter(pk=request.data.get('id', 0))
            serialized_data = UserSerializer(user_queryset.first(), data=request.data, partial=True)
            if serialized_data.is_valid():
                serialized_data.save()
                return ok(data=serialized_data.data)
        except Exception as er:
            print(str(er))
            return internal_server_error(data=[])

    def destroy(self, request, *args, **kwargs):
        try:
            user_queryset = User.objects.get(pk=request.query_params.get('id', 0))
            user_queryset.delete()
            return ok(data=[])
        except Exception as er:
            print(er)
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

    def list(self, request, *args, **kwargs):
        try:
            queryset = Group.objects.all()
            serialized_data = GroupSerializer(queryset, many=True)
            if serialized_data:
                return ok(data=serialized_data.data)
            else:
                return ok(data=[])
        except Exception as er:
            print(str(er))
            return internal_server_error(data=[])

    def update(self, request, *args, **kwargs):
        try:
            group_queryset = Group.objects.filter(pk=request.data.get('id', 0))
            serialized_data = GroupSerializer(group_queryset.first(), data=request.data, partial=True)
            if serialized_data.is_valid():
                serialized_data.save()
                return ok(data=serialized_data.data)
        except Exception as er:
            print(str(er))
            return internal_server_error(data=[])

    def destroy(self, request, *args, **kwargs):
        try:
            user_queryset = Group.objects.get(pk=request.query_params.get('id', 0))
            user_queryset.delete()
            return ok(data=[])
        except Exception as er:
            print(er)
            return internal_server_error(data=[])


class PermissionViews(viewsets.ModelViewSet):
    def list(self, request, *args, **kwargs):
        try:
            queryset = Permission.objects.all()
            serialized_data = PermissionSerializer(queryset, many=True)
            if serialized_data:
                return ok(data=serialized_data.data)
            else:
                return ok(data=[])
        except Exception as er:
            print(str(er))
            return internal_server_error(data=[])

    def create(self, request, *args, **kwargs):
        auth_user = request.user.has_perm("auth.add_permission")
        if auth_user:
            try:
                serialized_data = PermissionSerializer(data=request.data)
                if serialized_data.is_valid():
                    serialized_data.save()
                    return ok(data=serialized_data.data)
                else:
                    return ok(data=[])
            except Exception as er:
                print(str(er))
                return internal_server_error(data=[])
        else:
            return bad_request(data=[])
