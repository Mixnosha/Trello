from django.db import models


class Cards(models.Model):
    title = models.CharField(max_length=255)
    users = models.ManyToManyField(to='userApp.CustomUser', related_name='cards_users')
    admin_users = models.ManyToManyField(to='userApp.CustomUser', related_name='cards_adm')
    description = models.TextField(blank=True, null=True)
    comments = models.ManyToManyField(to='commentApp.Comment', related_name='cards_comment')

    def __str__(self):
        return self.title



