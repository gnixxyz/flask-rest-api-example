# coding: utf-8

from flask import request, current_app
from .app import make_app
from .import models, routes
from .ext import jwt


def set_development_env(app):
    from .ext import api_docs
    api_docs.init_app(app)

    @app.shell_context_processor
    def make_shell_context():
        return dict(
            app=app,
            db=models.db,
            User=models.User,
            Post=models.Post,
            PostLike=models.PostLike,
            Style=models.Style,
            Favorite=models.Favorite,
        )

    @app.cli.command()
    def initdb():
        import fixtures

        models.db.drop_all()
        models.db.create_all()
        fixtures.run()


def header_hook(response):
    remaining = getattr(request, '_rate_remaining', None)
    if remaining:
        response.headers['X-Rate-Limit'] = str(remaining)

    expires = getattr(request, '_rate_expires', None)
    if expires:
        response.headers['X-Rate-Expires'] = str(expires)

    # javascript can request API
    if request.method == 'GET':
        response.headers['Access-Control-Allow-Origin'] = '*'

    # api not available in iframe
    response.headers['X-Frame-Options'] = 'deny'
    # security protection
    if current_app.config['ENV'] == 'protection':
        response.headers['Content-Security-Policy'] = "default-src 'none'"
        response.headers['X-Content-Type-Options'] = 'nosniff'
    return response


def create_app(config=None):
    # make flask app
    app = make_app(config)

    # register models, routes
    models.init_app(app)
    routes.init_app(app)

    # register extensions
    jwt.init_app(app, models.func.user_loader)

    # header hook
    app.after_request(header_hook)

    # for development
    if app.config['ENV'] == 'development':
        set_development_env(app)

    return app
