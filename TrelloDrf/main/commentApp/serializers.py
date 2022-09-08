from rest_framework import serializers

from commentApp.models import Status


class StatusViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['title', 'description']
