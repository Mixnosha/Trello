from rest_framework import serializers

from columnApp.models import Column


class ColumnAllViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Column
        depth = 1
        fields = "__all__"