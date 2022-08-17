from django.db import models

class Column(models.Model):
    title = models.CharField(max_length=255)
    cards = models.ManyToManyField(to='cardsApp.Cards', related_name='column_cards')
    users = models.ManyToManyField(to='userApp.CustomUser', related_name='column_users')
    admin_users = models.ManyToManyField(to='userApp.CustomUser', related_name='column_adm')

    def __str__(self):
        return f'{self.title}'
