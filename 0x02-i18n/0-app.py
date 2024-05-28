#!/usr/bin/env python3
"""flask application"""
from flask import (flask, render_template)

app = Flask(__name__)


@app.route('/')
def index():
    """main route"""
    return render_template('index.html')


if __main__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
