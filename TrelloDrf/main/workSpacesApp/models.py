from django.db import models
from boardsApp.models import Boards
from userApp.models import CustomUser


class WorkSpaces(models.Model):
    TYPE = [
        (1, 'Малый Бизнес'),
        (2, 'Управление персоналом'),
        (3, 'Операции'),
        (4, 'Продажи CRM'),
        (5, 'Маркетинг'),
        (6, 'Инженерия IT'),
        (7, 'Образование'),
        (8, 'Другое'),

    ]
    title = models.CharField(max_length=100)
    short_title = models.CharField(max_length=50, unique=True)
    status = models.ForeignKey('Status', on_delete=models.CASCADE)
    boards = models.ManyToManyField(Boards, related_name='workspaces')
    users = models.ManyToManyField(CustomUser, related_name='workspaces')
    admin_users = models.ManyToManyField(CustomUser, related_name='workspaces')
    logo = models.ImageField(upload_to='', default='')
    type = models.CharField(choices=TYPE)
    web_site = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    join_link = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return f'WorkSpace: {self.title} admin: {self.admin_users[0].user.username}'


class Status(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title