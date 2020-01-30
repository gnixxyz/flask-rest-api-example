
from .base import db, Base
from .mixins import TimestampMixin, PasswordMixin


class User(Base, TimestampMixin, PasswordMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(128), nullable=False, unique=True)

    posts = db.relationship('Post', secondary='post_like', lazy='dynamic')
    styles = db.relationship('Style', secondary='favorite', lazy='dynamic')

    @classmethod
    def get_all(cls, ids):
        return cls.query.filter(cls.id.in_(ids)).all()

    def to_dict(self):
        return dict(id=self.id, name=self.name)
