
from flask import Blueprint, jsonify
from flask_apispec import doc, use_kwargs
from flask_jwt_extended import jwt_required, current_user
from webargs import fields
from ..import models, errors

app = Blueprint('post', __name__)


@doc(security=[{'bearer': []}], tags=['posts'])
@app.route('/')
@use_kwargs({
    'cursor': fields.Int(default=0),
    'limit': fields.Int(default=10),
    'order': fields.Str(default='desc'),
}, locations=['query'])
@jwt_required
def list_posts(cursor=0, limit=10, order='desc'):
    posts, cursor = models.func.cursor_query(
        models.Post, **{
            'cursor': cursor,
            'limit': limit,
            'order': order,
        }
    )

    data = list(models.func.iter_items_with_users(posts))

    return jsonify(data=data, cursor=cursor)


@doc(security=[{'bearer': []}], tags=['posts'])
@app.route('/<int:id>')
@jwt_required
def view_post(id):
    result = models.Post.query\
        .filter(models.Post.id == id)\
        .join(models.User, models.User.id == models.Post.user_id)\
        .add_entity(models.User)\
        .first()

    if not result:
        raise errors.NotFound(id)

    data = result.Post.to_dict()
    data['user'] = result.User.to_dict()

    return jsonify(data=data)
