# This file initializes your application and brings together all of the various components.
import connexion
from connexion.resolver import RestyResolver
from nasdaq.views import home, scraper
from nasdaq.models.nasdaq import MostActive, db

app = connexion.App(__name__, specification_dir='swagger/')
app.add_api('swagger.yaml', resolver=RestyResolver('api'))

app.register_blueprint(home.home_bp, url_prefix='/')
app.register_blueprint(scraper.scraper_bp, url_prefix='/scraper')


app.config.from_object('config')
app.config.from_pyfile('config.py')

db.init_app(app)

