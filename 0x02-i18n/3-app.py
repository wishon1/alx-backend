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


# @babel.localeselector( am commeting it because of this error):
# ack (most recent call last):
#  File "/usr/lib/python3.8/runpy.py", line 194, in _run_module_as_main
#    return _run_code(code, main_globals, None,
#  File "/usr/lib/python3.8/runpy.py", line 87, in _run_code
#    exec(code, run_globals)
#  File "/home/pc/alx-backend/0x02-i18n/3-app.py", line 29, in <module>
#    @babel.localeselector
# AttributeError: 'Babel' object has no attribute 'localeselector'

@babel.localeselector
def get_locale() -> str:
    """Determine the best match for the supported language"""
    return request.accept_language.best_match(app.config['LANGUAGES'])


# @babel.localeselector is not supported in newer versions of babel.
# use this instead
# babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def index() -> str:
    """main route"""
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
