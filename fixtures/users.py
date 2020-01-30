# coding: utf-8

import random
from web.models import User
from .base import fake


def iter_special_users():
    yield {
        "name": "sushi",
        "email": "sushi@example.com",
    }

    yield {
        "name": "kingkong",
        "email": "kingkong@example.com",
    }

    yield {
        "name": "test",
        "email": "test@example.com",
    }


def iter_normal_users():
    domains = ['gmail.com', 'hotmail.com', 'yahoo.com', 'outlook.com']

    for i in range(3, 1024):
        name = fake.first_name()
        yield {
            "name": name,
            "email": '{}@{}'.format(name, random.choice(domains)),
        }


def iter_data():
    for data in iter_special_users():
        user = User(**data)
        user.password = '1'
        yield user
    for data in iter_normal_users():
        yield User(**data)
