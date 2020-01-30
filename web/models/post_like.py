# coding: utf-8

from .base import db, Base
from .mixins import CreateTimeMixin


class PostLike(Base, CreateTimeMixin):
    __tablename__ = 'post_like'

    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)

    post = db.relationship('Post', backref=db.backref(
        "likes", cascade="all, delete-orphan"))
    user = db.relationship('User', backref=db.backref(
        "likes", cascade="all, delete-orphan"))

    def __init__(self, post_id, user_id):
        self.post_id = post_id
        self.user_id = user_id
