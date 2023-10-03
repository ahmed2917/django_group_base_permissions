# generic response are written to return error message to frontend
from rest_framework.response import Response


def ok(data=None, message='Success'):
    return Response(status=200, data={'error': False, 'result': data, 'message': message, 'statusCode': 200})


def created(data=None, message='Successfully created'):
    return Response(status=201, data={'error': False, 'result': data, 'message': message, 'statusCode': 201})


def bad_request(data=None, message='Bad request'):
    return Response(status=400, data={'error': True, 'result': data, 'message': message, 'statusCode': 400})


def unauthorized(data=None, message='Unauthorized'):
    return Response(status=401, data={'error': True, 'result': data, 'message': message, 'statusCode': 401})


def not_found(data=None, message='Not found'):
    return Response(status=404, data={'error': True, 'result': data, 'message': message, 'statusCode': 404})


def conflict(data=None, message='Already exists'):
    return Response(status=409, data={'error': True, 'result': data, 'message': message, 'statusCode': 409})


def internal_server_error(data=None, message='Something went wrong'):
    return Response(status=500, data={'error': True, 'result': data, 'message': message, 'statusCode': 500})
