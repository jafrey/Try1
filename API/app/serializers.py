from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.response import Response
from .models import Cancion


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password']

class CancionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cancion
        fields = ['id', 'nom_cancion']
