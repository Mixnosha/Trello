from django.contrib.auth.models import User
from django.db import IntegrityError
from authUser.forms import UserRegisterForm
from userApp.models import CustomUser


def registerUser(data):
    """Функция регистрации"""
    try:
        first_name = data['first_name']
        data.pop('first_name')
        try:
            User.objects.get(username=data['username'])
            return 123
        except Exception:
            pass
        form = UserRegisterForm(data)
        form.save()
        user = User.objects.get(username=data['username'])
        CustomUser.objects.create(user=user, first_name=first_name)
        return True
    except IntegrityError:
        return 101
    except Exception as e:
        return e


