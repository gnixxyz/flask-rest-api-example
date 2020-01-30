
from .base import db, Base
from .mixins import TimestampMixin


class Post(Base, TimestampMixin):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140), nullable=False)
    content = db.Column(db.Text, default=None)
    user_id = db.Column(db.Integer, nullable=False, index=True)

    users = db.relationship('User', secondary='post_like', lazy='dynamic')

    def to_dict(self):
        return dict(id=self.id, title=self.title, content=self.content)
