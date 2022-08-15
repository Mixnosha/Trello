from django.db import models

from userApp.models import CustomUser


class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL)
    text = models.TextField()
    data = models.DateField(auto_created=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.user.username} data {self.data}'