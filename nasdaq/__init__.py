# This file initializes your application and brings together all of the various components.
from flask import Flask
from nasdaq.views import home, scraper
from nasdaq.models.nasdaq import MostActive, db

app = Flask(__name__, instance_relative_config=True)

app.register_blueprint(home.home_bp, url_prefix='/')
app.register_blueprint(scraper.scraper_bp, url_prefix='/scraper')


app.config.from_object('config')
app.config.from_pyfile('config.py')

db.init_app(app)

