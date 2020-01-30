

import marshmallow as ma


class CursorMixin(ma.Schema):
    cursor = ma.fields.Integer(default=0)
    limit = ma.fields.Integer(default=10)


class Style(ma.Schema):
    id = ma.fields.Integer()
    name = ma.fields.String()
    url = ma.fields.Url()
    price = ma.fields.DateTime()


class ViewStyle(ma.Schema):
    data = ma.fields.Nested(Style)


class ListStyles(ma.Schema):
    data = ma.fields.Nested(Style(many=True))
    cursor = ma.fields.Integer()
