from django.db import models

from cardsApp.models import Cards
from userApp.models import CustomUser


class Column(models.Model):
    title = models.CharField(max_length=255)
    cards = models.ManyToManyField(Cards, related_name='column')
    users = models.ManyToManyField(CustomUser, related_name='column')
    admin_users = models.ManyToManyField(CustomUser, related_name='column')

    def __str__(self):
        return f'{self.title}'
