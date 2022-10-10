from django.db import models

class Boards(models.Model):
    users = models.ManyToManyField(to='userApp.CustomUser', related_name='boards_users', blank=True)
    admin_users = models.ManyToManyField(to='userApp.CustomUser', related_name='boards_adm')
    title = models.CharField(max_length=255)
    column = models.ManyToManyField(to='columnApp.Column', blank=True, related_name='boards_column')
    join_link = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    background = models.CharField(max_length=20, blank=True, null=True, default="#f67272")
    status = models.ForeignKey('status.StatusBoards', on_delete=models.CASCADE)
    slug = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'Boards {self.title}' + " " + str(self.id)



