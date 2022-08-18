from django.contrib.auth.models import User
from django.db import models

class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    about = models.TextField(blank=True, null=True)
    favorites_boards = models.ManyToManyField(to='boardsApp.Boards', related_name='user', blank=True)

    def __str__(self):
        return self.user.username

