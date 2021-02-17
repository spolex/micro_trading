from injector import Binder
from selenium.webdriver import Firefox, FirefoxOptions
from nasdaq import create_app
from flask_injector import FlaskInjector


def configure(binder: Binder) -> Binder:
    options = FirefoxOptions()
    options.add_argument("--headless")
    binder.bind(
        Firefox,
        Firefox(options=options)
    )
    return binder


if __name__ == '__main__':
    app = create_app()
    FlaskInjector(app=app.app, modules=[configure])
    app.run(port=5000, host='0.0.0.0')
