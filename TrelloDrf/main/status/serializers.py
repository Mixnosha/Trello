from rest_framework import serializers
from status.models import StatusWK


class StatusViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusWK
        fields = ['id', 'title', 'description', 'icon']
