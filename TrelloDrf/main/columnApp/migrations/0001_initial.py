# Generated by Django 4.1 on 2022-08-17 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userApp', '0001_initial'),
        ('cardsApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('admin_users', models.ManyToManyField(related_name='column_adm', to='userApp.customuser')),
                ('cards', models.ManyToManyField(related_name='column_cards', to='cardsApp.cards')),
                ('users', models.ManyToManyField(related_name='column_users', to='userApp.customuser')),
            ],
        ),
    ]