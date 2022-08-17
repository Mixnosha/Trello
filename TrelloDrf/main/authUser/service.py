from django.contrib.auth.models import User
from django.db import IntegrityError

from userApp.models import CustomUser


def registerUser(data):
    try:
        User.objects.create(username=data['username'], email=data['email'], password=data['password'])
        # CustomUser.objects.create()
        return True
    except IntegrityError:
        return 'A user with the same name already exists'
    except Exception:
        return False


