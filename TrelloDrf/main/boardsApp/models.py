from django.db import models
from columnApp.models import Column
from userApp.models import CustomUser
from workSpacesApp.models import Status


class Boards(models.Model):
    users = models.ManyToManyField(CustomUser, related_name='boards')
    admin_users = models.ManyToManyField(CustomUser, related_name='boards')
    title = models.CharField(max_length=255)
    private_users = models.ManyToManyField(CustomUser, related_name='boards')
    column = models.ManyToManyField(Column, related_name='boards')
    join_link = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    background = models.ImageField(upload_to='', default='')
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return f'Boards {self.title} admin {self.admin_users[0].user.username}'



