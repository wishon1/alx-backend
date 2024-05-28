#!/usr/bin/env python3
"""flask application with babel for i18n"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """config class for the Flask application"""
    # specify the supported languages for the app
    LANGUAGES = ["en", "fr"]

    # set the defualt locale (language) to English
    BABEL_DEFAULT_LOCALE = "en"

    # set the defualt timezone to UTC
    BABEL_DEFUALT_TIMEZONE = "UTC"


# Apply the configuration settings to the flask app
app.config.from_object(Config)

# instantiate the Babel object and pass the Flask app instance to it
babel = Babel(app)


@app.route('/', strict_slashes=False)
def index() -> str:
    """main route"""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
