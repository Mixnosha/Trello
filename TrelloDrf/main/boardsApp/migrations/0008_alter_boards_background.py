# Generated by Django 4.1 on 2022-10-10 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardsApp', '0007_alter_boards_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boards',
            name='background',
            field=models.CharField(blank=True, default='#f67272', max_length=20, null=True),
        ),
    ]
