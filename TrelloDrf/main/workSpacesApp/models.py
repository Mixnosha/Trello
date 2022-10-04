from django.db import models

from workSpacesApp.service import get_slug


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
    status = models.ForeignKey(to='status.StatusWK', on_delete=models.CASCADE)
    boards = models.ManyToManyField(to='boardsApp.Boards', related_name='workspaces_boards', blank=True)
    users = models.ManyToManyField(to='userApp.CustomUser', related_name='workspaces_users', blank=True)
    admin_users = models.ManyToManyField(to='userApp.CustomUser', related_name='workspaces_adm')
    logo = models.ImageField(upload_to='', default='', blank=True)
    type = models.IntegerField(choices=TYPE)
    web_site = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    join_link = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return f'WorkSpace: {self.title}' + str(self.id)

    def save(self, *args, **kwargs):
        if self.title and self.id:
            self.slug = get_slug(self.title) + str(self.id)
        super(WorkSpaces, self).save(*args, **kwargs)



