from django.shortcuts import render
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from . import utils


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


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_profile(request):
    user = request.user
    editables = ['first_name', 'phone', 'address', 'email']
    res = {'message': 'Profile updated successfully'}
    for field in editables:
        if request.data.get(field):
            setattr(user, field, request.data.get(field))
    if avatar_b64:=request.data.get('avatar_b64'):
        try:
            avatar = utils.get_base64_image_file(avatar_b64)
            user.avatar = avatar
        except Exception as e:
            res['message'] = f"Profile updated but error in updating avatar"
    user.save()
    return Response(res)