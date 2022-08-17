from django.db import models

class Boards(models.Model):
    users = models.ManyToManyField(to='userApp.CustomUser', related_name='boards_users')
    admin_users = models.ManyToManyField(to='userApp.CustomUser', related_name='boards_adm')
    title = models.CharField(max_length=255)
    private_users = models.ManyToManyField(to='userApp.CustomUser', related_name='boards_privat')
    column = models.ManyToManyField(to='columnApp.Column', related_name='boards_column')
    join_link = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    background = models.ImageField(upload_to='', default='')
    status = models.ForeignKey('commentApp.Status', on_delete=models.CASCADE)

    def __str__(self):
        return f'Boards {self.title} admin {self.admin_users[0].user.username}'



