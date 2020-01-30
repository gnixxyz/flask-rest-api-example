
from flask_jwt_extended import JWTManager

jwt = JWTManager()


def init_app(app, user_loader):
    jwt.init_app(app)
    jwt.user_loader_callback_loader(user_loader)
