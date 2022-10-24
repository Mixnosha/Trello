from django.db import models


class Cards(models.Model):
    title = models.CharField(max_length=255)
    users = models.ManyToManyField(to='userApp.CustomUser', related_name='cards_users', blank=True, null=True)
    admin_users = models.ManyToManyField(to='userApp.CustomUser', related_name='cards_adm', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    comments = models.ManyToManyField(to='commentApp.Comment', related_name='cards_comment', blank=True, null=True)

    def __str__(self):
        return self.title + ' id' + f' {self.id}'



