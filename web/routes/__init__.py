# coding: utf-8


def init_app(app):
    from .import home, auth, user, style, post

    app.register_blueprint(home.app, url_prefix='')
    app.register_blueprint(auth.app, url_prefix='/auth')
    app.register_blueprint(user.app, url_prefix='/users')
    app.register_blueprint(style.app, url_prefix='/styles')
    app.register_blueprint(post.app, url_prefix='/post')
