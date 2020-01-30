# coding: utf-8

from web.models import Style
from .base import fake


def iter_styles():
    for i in range(1, 1024):
        yield {
            "name": fake.safe_color_name(),
            "url": fake.image_url(),
            "price": fake.random_int(min=0, max=9999, step=1),
        }


def iter_data():
    for data in iter_styles():
        yield Style(**data)
