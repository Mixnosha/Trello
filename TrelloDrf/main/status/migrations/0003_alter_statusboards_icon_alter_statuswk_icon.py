# Generated by Django 4.1 on 2022-10-10 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0002_alter_statusboards_icon_alter_statuswk_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statusboards',
            name='icon',
            field=models.FileField(blank=True, null=True, upload_to='data/statusBoards/icons'),
        ),
        migrations.AlterField(
            model_name='statuswk',
            name='icon',
            field=models.FileField(blank=True, null=True, upload_to='data/statusBoards/icons'),
        ),
    ]