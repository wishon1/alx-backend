#!/usr/bin/env python3
"""A simple Flask app with Babel for i18n support"""

from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config(object):
    """
    Configuration class for the Flask application.

    Attributes:
        LANGUAGES (list): Supported languages for the app.
        BABEL_DEFAULT_LOCALE (str): Default locale for the app.
        BABEL_DEFAULT_TIMEZONE (str): Default timezone for the app.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Configure the Flask app
app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False

# Instantiate the Babel object and pass the Flask app instance to it
babel = Babel(app)

# Mock user data
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """
    Retrieves a user dictionary based on a login ID provided as a query
    parameter.

    Returns:
        dict: User information dictionary or None if the user ID is not found.
    """
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None


@app.before_request
def before_request() -> None:
    """
    Hook that runs before each request to set the current user in the global
    context.
    """
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale():
    """
    Selects the best match for the supported languages based on the request.

    It checks for a 'locale' parameter in the URL, user settings, request
    headers, and defaults to the best match from the accepted languages.

    Returns:
        str: The best matching locale.
    """
    # Locale from URL parameters
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    # Locale from user settings
    if g.user:
        locale = g.user.get('locale')
        if locale and locale in app.config['LANGUAGES']:
            return locale

    # Locale from request headers
    locale = request.headers.get('locale', None)
    if locale in app.config['LANGUAGES']:
        return locale

    # Default locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


# Initialize Babel with the locale selector function
# babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def index():
    """
    Main route that renders the index page.

    Returns:
        str: Rendered HTML template for the index page.
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
