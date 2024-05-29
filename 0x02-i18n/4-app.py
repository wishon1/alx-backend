#!/usr/bin/env python3
"""flask application with babel for i18n"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """config class for the Flask application"""
    # specify the supported languages for the app
    LANGUAGES = ["en", "fr"]

    # set the defualt locale (language) to English
    BABEL_DEFAULT_LOCALE = "en"

    # set the defualt timezone to UTC
    BABEL_DEFUALT_TIMEZONE = "UTC"


app = Flask(__name__)

# Apply the configuration settings to the flask app
app.config.from_object(Config)
app.url_map.strict_slashes = False

# instantiate the Babel object and pass the Flask app instance to it
babel = Babel(app)


# @babel.localeselector
def get_locale() -> str:
    """
    detect if the incoming request contains locale argument and ifs value is
    a supported locale, return it. If not or if the parameter is not present,
    resort to the previous default behavior
    """
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        print(locale)
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def index() -> str:
    """main route"""
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
