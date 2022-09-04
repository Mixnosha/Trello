# Generated by Django 4.1 on 2022-08-18 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardsApp', '0002_initial'),
        ('userApp', '0004_alter_customuser_favorites_boards'),
        ('workSpacesApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workspaces',
            name='boards',
            field=models.ManyToManyField(blank=True, related_name='workspaces_boards', to='boardsApp.boards'),
        ),
        migrations.AlterField(
            model_name='workspaces',
            name='logo',
            field=models.ImageField(blank=True, default='', upload_to=''),
        ),
        migrations.AlterField(
            model_name='workspaces',
            name='type',
            field=models.CharField(choices=[(1, 'Малый Бизнес'), (2, 'Управление персоналом'), (3, 'Операции'), (4, 'Продажи CRM'), (5, 'Маркетинг'), (6, 'Инженерия IT'), (7, 'Образование'), (8, 'Другое')], max_length=255),
        ),
        migrations.AlterField(
            model_name='workspaces',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='workspaces_users', to='userApp.customuser'),
        ),
    ]