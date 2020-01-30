
from .base import db, Base
from .mixins import CreateTimeMixin


class Style(Base, CreateTimeMixin):
    __tablename__ = 'style'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, unique=True)
    url = db.Column(db.String(1024), nullable=False)
    price = db.Column(db.Float, default=0)

    users = db.relationship('User', secondary='favorite', lazy='dynamic')

    @classmethod
    def get_all(cls, ids):
        return cls.query.filter(cls.id.in_(ids)).all()

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            url=self.url,
            price=self.price,
            created_at=self.created_at,
        )
