# coding: utf-8
# flake8: noqa

from .base import db
from .user import User
from .post import Post
from .post_like import PostLike
from .style import Style
from .favorite import Favorite
from .import func


def init_app(app):
    db.init_app(app)
