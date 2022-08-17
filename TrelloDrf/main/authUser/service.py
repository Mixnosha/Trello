from django.contrib.auth.models import User


def registerUser(data):
    User.objects.create(username=data['username'], email=data['email'], password=data['password'])
