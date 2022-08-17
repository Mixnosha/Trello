from django.contrib.auth.models import User
from django.db import IntegrityError
from authUser.forms import UserRegisterForm
from userApp.models import CustomUser


def registerUser(data):
    try:
        form = UserRegisterForm(data)
        form.save()
        o
        user = User.objects.get(username=data['username'])
        CustomUser.objects.create(user=user.username, first_name=data['first_name'])
        return True
    except IntegrityError:
        return 'A user with the same name already exists'
    except Exception as e:
        print(e)
        return False


