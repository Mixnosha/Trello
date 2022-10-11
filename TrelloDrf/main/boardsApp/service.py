import random

from boardsApp.models import Boards
from workSpacesApp.models import WorkSpaces


def get_slug_board(title: str) -> str:
    "генерирует slug на по принципу title='maKs top'  slug = maks_top'рандомные буквы в рандомном регистре')"
    alph = 'abcdefghijklmnopqrstuvwxyz'
    title = title.split()
    slug = ''
    for i in title:
        slug += i.lower() + "_"

    slug = slug[:-1]
    rand = random.randint(5, 7)
    for i in range(rand):
        x = random.randint(0, 1)
        if x == 1:
            slug += alph[random.randint(0, len(alph)-1)].upper()
        else:
            slug += alph[random.randint(0, len(alph)-1)]
    return slug


def get_board_to_slug_funck(slug: str):
    b = Boards.objects.get(slug=slug)
    w = WorkSpaces.objects.get(boards=b)
    return b, w