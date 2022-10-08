from django.db import models

class Status(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.id) + ' ' + self.title

class StatusBoards(Status):
    icon = models.FileField(upload_to=f'data/statusBoards/icons', blank=True, null=True)

class StatusWK(Status):
    icon = models.FileField(upload_to=f'data/statusBoards/icons', blank=True, null=True)


