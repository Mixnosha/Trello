from rest_framework import serializers
from userApp.models import CustomUser


class CustomUserViewAllSerializer(serializers.ModelSerializer):
    """"""
    user = serializers.CharField()

    class Meta:
        model = CustomUser
        fields = ['user']
