# coding: utf-8

from .base import db, Base
from .mixins import CreateTimeMixin


class Favorite(Base, CreateTimeMixin):
    __tablename__ = 'favorite'

    style_id = db.Column(db.Integer,
                         db.ForeignKey('style.id'),
                         primary_key=True)
    user_id = db.Column(db.Integer,
                        db.ForeignKey('user.id'),
                        primary_key=True)

    style = db.relationship('Style', backref=db.backref(
        "favorite", cascade="all, delete-orphan", lazy='dynamic'))
    user = db.relationship('User', backref=db.backref(
        "favorite", cascade="all, delete-orphan", lazy='dynamic'))

    def __init__(self, style_id, user_id):
        self.style_id = style_id
        self.user_id = user_id
