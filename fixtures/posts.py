# coding: utf-8


import random
from web.models import Post, PostLike, Favorite

from .base import fake


def create_post(user_id):
    return {
        "title": fake.slug(),
        "user_id": user_id,
        "content": fake.name(),
    }


def iter_user_posts():
    print('Creating posts')
    for i in range(1, 500):
        yield create_post(random.randint(1, 500))
    for i in range(500, 1000):
        yield create_post(random.randint(1, 3))


def iter_post_likes():
    print('Creating post likes')
    for i in range(1, 2000):
        yield {
            "post_id": random.randint(1, 62),
            "user_id": random.randint(1, 100),
        }


def iter_user_favorites():
    print('Creating style favorites')
    for i in range(1, 2000):
        yield {
            "style_id": random.randint(1, 62),
            "user_id": random.randint(1, 100),
        }


def iter_data():
    for data in iter_user_posts():
        yield Post(**data)

    for data in iter_post_likes():
        yield PostLike(**data)

    for data in iter_user_favorites():
        yield Favorite(**data)
