from rest_framework import serializers

from boardsApp.models import Boards
from cardsApp.models import Cards
from columnApp.models import Column
from userApp.models import CustomUser


class OneCardViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cards
        fields = '__all__'


class AllCardViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cards
        fields = ['id', 'title']


class CreateCardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cards
        fields = ['id', 'title']

    def create(self, validated_data):
        adm_user = CustomUser.objects.get(user__username=self.context['request'].user)
        card = Cards.objects.create(
            **validated_data,
        )
        card.admin_users.add(adm_user.id)
        card.save()
        clmn = Column.objects.get(id=self.context['request'].data['clmn_id'])
        clmn.cards.add(card.id)
        clmn.save()
        return card


class UpdateCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cards
        fields = ['id', 'title', 'description']