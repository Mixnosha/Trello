from django.contrib.auth.models import User
from django.db import IntegrityError
from authUser.forms import UserRegisterForm
from userApp.models import CustomUser
from django.contrib.auth import authenticate


def registerUser(data):
    try:
        first_name = data['first_name']
        data.pop('first_name')
        print(data)
        form = UserRegisterForm(data)
        form.save()
        user = User.objects.get(username=data['username'])
        CustomUser.objects.create(user=user, first_name=first_name)
        return True
    except IntegrityError:
        return 'A user with the same name already exists'
    except Exception as e:
        print(e)
        return False

def login(data):
    try:
        user = authenticate(username=data['username'], password=data['password'])
        if user is not None:
            print('Triuuere')
        else:
            print('flaser')
    except Exception as e:
        print(e)


