import random


def get_slug(title):
    title = title.split()
    slug = ''
    max_count = len(title) - 1
    for i, word in enumerate(title):
        if i == max_count:
            slug += word.lower()
            break
        slug += word + '_'
    return slug






