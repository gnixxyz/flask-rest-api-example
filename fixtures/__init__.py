# coding: utf-8

from sqlalchemy.exc import IntegrityError
from web.models import db


def commit(module):
    for mod in module.iter_data():
        db.session.add(mod)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()


def run():
    from . import users, styles, posts

    for m in [users, styles, posts]:
        commit(m)
