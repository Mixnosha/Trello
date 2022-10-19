from django.db import models


class Column(models.Model):
    title = models.CharField(max_length=255)
    cards = models.ManyToManyField(to='cardsApp.Cards', related_name='column_cards', blank=True, null=True)
    users = models.ManyToManyField(to='userApp.CustomUser', related_name='column_users', blank=True, null=True)
    admin_users = models.ManyToManyField(to='userApp.CustomUser', related_name='column_adm', blank=True, null=True)

    def __str__(self):
        return f'{self.title}' + f'  id: {self.id}'
