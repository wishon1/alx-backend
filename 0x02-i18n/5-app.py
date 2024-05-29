#!/usr/bin/env python3
"""flask application with babel for i18n"""
from flask import Flask, render_template, request, g
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


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """
    returns a user dictionary or None if the ID cannot be found or if
    login_as was not passed.
    """
    user_login_id = request.args.get('login_as')
    if user_login_id:
        return users.get(int(user_login_id))
    return None


@app.before_request
def before_request() -> None:
    """
    use get_user to find a user if any, and set it as a global on
    flask.g.user
    """
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale() -> str:
    """Retrieve the locale(language) for the web page"""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        print(locale)
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


# babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def index() -> str:
    """main route"""
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
