from django.db import models

from commentApp.models import Comment
from userApp.models import CustomUser


class Cards(models.Model):
    title = models.CharField(max_length=255)
    users = models.ManyToManyField(CustomUser, related_name='cards')
    admin_users = models.ManyToManyField(CustomUser, related_name='cards')
    description = models.TextField(blank=True, null=True)
    comments = models.ManyToManyField(Comment, related_name='cards')

    def __str__(self):
        return self.title



