# This file initializes your application and brings together all of the various components.
import connexion
from connexion.resolver import RestyResolver
from nasdaq.api import home
from nasdaq.models.nasdaq import MostActive, db
from json import JSONEncoder


def create_app():
    """

    :return:
    """
    app = connexion.App(__name__, specification_dir='../swagger/')

    # This allows the connexion models to be serialized to JSON
    app.json_encoder = JSONEncoder

    # normal configuration

    # The return value is a `connexion.Api`.
    # If needed, the api blueprint is available at `connexion.Api.blueprint`
    app.add_api('swagger.yaml', resolver=RestyResolver('api'))
    # app.config.from_object('config')
    # app.config.from_pyfile('config.py')

    # db.init_app(app)

    return app

