
from webargs import fields

from flask import Blueprint, jsonify
from flask_apispec import doc, use_kwargs
from flask_jwt_extended import create_access_token

from ..import models, errors

app = Blueprint('auth', __name__)


@doc(tags=['auth'])
@app.route('/login', methods=['POST'])
@use_kwargs({
    'username': fields.Str(),
    'password': fields.Str(),
}, locations=['form'])
def login(username, password):
    user = models.User.query.filter_by(email=username).first()

    if not user or not user.check_password(password):
        raise errors.InvalidAccount()

    access_token = create_access_token(user.id)
    return jsonify(access_token=access_token, token_type='bearer')


@doc(tags=['auth'])
@app.route('/logout', methods=['GET', 'POST'])
def logout():
    return jsonify(data='comming soon!')
