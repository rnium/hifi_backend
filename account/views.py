from django.shortcuts import render
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['POST'])
def admin_token_login(request):
    user = authenticate(
        request, 
        email=request.data.get('email'),
        password=request.data.get('password'),
    )
    print(user)
    if user is None or not user.is_staff:
        return Response({'non_field_errors': ['Cannot login as admin']}, status=status.HTTP_401_UNAUTHORIZED)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'auth_token': token.key})