#!/usr/bin/env python3
"""flask application"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index() -> str:
    """main route"""
    return render_template('0-index.html')


if __main__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
