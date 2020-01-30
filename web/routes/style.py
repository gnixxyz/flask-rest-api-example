
from flask import Blueprint, jsonify
from flask_apispec import doc, use_kwargs
from flask_jwt_extended import jwt_required, current_user
from webargs import fields
from ..import models, errors

app = Blueprint('style', __name__)


@doc(security=[{'bearer': []}], tags=['styles'])
@app.route('/')
@use_kwargs({
    'cursor': fields.Int(default=0),
    'limit': fields.Int(default=10),
    'order': fields.Str(default='desc'),
}, locations=['query'])
@jwt_required
def list_styles(cursor=0, limit=10, order='desc'):
    styles, cursor = models.func.cursor_query(
        models.Style, **{
            'cursor': cursor,
            'limit': limit,
            'order': order,
        }
    )

    return jsonify(data=styles, cursor=cursor)


@doc(security=[{'bearer': []}], tags=['styles'])
@app.route('/<int:id>')
@jwt_required
def view_style(id):
    style = models.Style.query.get(id)

    if not style:
        raise errors.NotFound(id)

    return jsonify(data=style)


@doc(security=[{'bearer': []}], tags=['styles'])
@app.route('/<int:id>/favorite', methods=['POST'])
@jwt_required
def favorite_style(id):
    favorite = models.Favorite.query.get((id, current_user.id))

    if favorite:
        raise errors.Conflict(description='Your already favorite it.')

    style = models.Style.query.get(id)

    if not style:
        raise errors.NotFound(id)

    favorite = models.Favorite(style.id, current_user.id)
    with models.db.auto_commit():
        models.db.session.add(favorite)

    return '', 204


@doc(security=[{'bearer': []}], tags=['styles'])
@app.route('/<int:id>/favorite', methods=['DELETE'])
@jwt_required
def unfavorite_style(id):
    favorite = models.Favorite.query.get((id, current_user.id))

    if not favorite:
        raise errors.Conflict(description='Your already unfavorite it.')

    with models.db.auto_commit():
        models.db.session.delete(favorite)

    return '', 204
