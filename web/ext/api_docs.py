# coding: utf-8

from flask_apispec import FlaskApiSpec

docs = FlaskApiSpec()


def init_app(app, with_default_register=True):
    from apispec import APISpec
    from apispec.ext.marshmallow import MarshmallowPlugin

    security_definitions = {
        "bearer": {
            "type": "oauth2",
            "flow": "password",
            "tokenUrl": "/auth/login",
        }
    }

    app.config.update({
        'APISPEC_SPEC': APISpec(
            title='FLASK-APP',
            version='v1',
            plugins=[MarshmallowPlugin()],
            openapi_version='2.0',
            securityDefinitions=security_definitions,
        ),
        'APISPEC_SWAGGER_URL': '/api-spec/',
        'APISPEC_SWAGGER_UI_URL': '/api/',
    })

    docs.init_app(app)

    if with_default_register:
        docs.register_existing_resources()
