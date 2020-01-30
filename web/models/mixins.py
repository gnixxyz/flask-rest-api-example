# coding: utf-8

from datetime import datetime
from sqlalchemy import Column, DateTime, String
from sqlalchemy.ext.declarative import declared_attr
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash


class CreateTimeMixin(object):
    @declared_attr
    def created_at(cls):
        return Column(DateTime, default=datetime.utcnow)


class TimestampMixin(CreateTimeMixin):
    @declared_attr
    def updated_at(cls):
        return Column(DateTime,
                      default=datetime.utcnow,
                      onupdate=datetime.utcnow)


class PasswordMixin(object):
    @declared_attr
    def _password(cls):
        return Column('password', String(255))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw_password):
        self._password = generate_password_hash(raw_password)

    def check_password(self, raw_password):
        if not self._password:
            return False
        return check_password_hash(self._password, raw_password)
