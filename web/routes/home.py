# coding: utf-8

from webargs import fields
from flask import Blueprint, jsonify
from flask_apispec import doc, use_kwargs
from flask_jwt_extended import jwt_required, current_user

from ..import errors

app = Blueprint('home', __name__)


@app.route('/')
def index():
    return jsonify(data='Welcome to flaskapp')


@app.route('/ping')
def ping():
    return jsonify(data='pong')


@doc(security=[{'bearer': []}])
@app.route('/test')
@use_kwargs({
    'Authorization':
        fields.Str(
            required=True,
            description='Authorization HTTP header with JWT refresh token, \
                like: Authorization: Bearer asdf.qwer.zxcv'
        )
}, locations=['headers'])
@jwt_required
def test(**kwargs):
    if not current_user:
        raise errors.NotAuth()
    return jsonify(data=current_user)
