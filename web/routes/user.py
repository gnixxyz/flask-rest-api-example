
from flask import Blueprint, jsonify
from flask_apispec import doc, use_kwargs
from flask_jwt_extended import jwt_required, current_user
from webargs import fields
from ..import models, errors

app = Blueprint('user', __name__)


@doc(security=[{'bearer': []}], tags=['users'])
@app.route('/me')
@jwt_required
def view_current_user():
    return jsonify(data=current_user)


@doc(security=[{'bearer': []}], tags=['users'])
@app.route('/<username>')
@jwt_required
def view_user(username):
    user = models.User.query.filter_by(name=username).first()
    if not user:
        raise errors.NotFound(username)

    return jsonify(data=user)


@doc(security=[{'bearer': []}], tags=['users'])
@app.route('/<username>/favorite')
@use_kwargs({
    'page': fields.Int(default=1),
    'per_page': fields.Int(default=10),
    'order': fields.Str(default='desc'),
}, locations=['query'])
@jwt_required
def view_user_favorite(username, page=1, per_page=10, order='desc'):
    user = models.User.query.filter_by(name=username).first()

    if not user:
        raise errors.NotFound(username)

    p = user.styles.paginate(page, per_page, False)

    paginate = {
        'total': p.total,
        'next': p.next_num,
        'prev': p.prev_num,
        'page': page,
        'per_page': p.per_page,
    }

    return jsonify(data=p.items, paginate=paginate)


@doc(security=[{'bearer': []}], tags=['users'])
@app.route('/<username>/likes')
@use_kwargs({
    'page': fields.Int(default=1),
    'per_page': fields.Int(default=10),
    'order': fields.Str(default='desc'),
}, locations=['query'])
@jwt_required
def view_user_likes(username, page=1, per_page=10, order='desc'):
    user = models.User.query.filter_by(name=username).first()

    if not user:
        raise errors.NotFound(username)

    p = user.posts.paginate(page, per_page, False)

    data = list(models.func.iter_items_with_users(p.items))

    paginate = {
        'total': p.total,
        'next': p.next_num,
        'prev': p.prev_num,
        'page': page,
        'per_page': p.per_page,
    }

    return jsonify(data=data, paginate=paginate)
