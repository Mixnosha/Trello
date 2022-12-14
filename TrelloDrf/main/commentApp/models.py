from django.db import models

class Comment(models.Model):
    user = models.ForeignKey(to='userApp.CustomUser', null=True, on_delete=models.SET_NULL)
    text = models.TextField()
    data = models.DateField(auto_created=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.user.username} data {self.data}'


