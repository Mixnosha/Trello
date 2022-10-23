from rest_framework import serializers

from cardsApp.models import Cards


class OneCardViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cards
        fields = '__all__'
