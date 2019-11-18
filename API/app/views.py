from django.shortcuts import render, render_to_response
from .serializers import UserSerializer, CancionSerializer
from rest_framework import viewsets, generics
from .models import Cancion
from django.contrib.auth.models import User

from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

from rest_framework.response import Response


#Para ver si el man esta autenticado
from rest_framework.permissions import IsAuthenticated

#para ejemplo

from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.


class UserViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)


@csrf_exempt
@api_view(["GET"])
def HelloView(request):
        content = {'message': 'Hello, World!'}
        return Response(content, status=HTTP_200_OK)


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))

def login(request):

    username = request.data.get("username")
    password = request.data.get("password")

    if username is "" or password is "":
        return Response({'error': 'Nigún campo puede estar vacio idiota.'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'A quien te crees que cagas, lo que pusiste no existe crack.'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)
