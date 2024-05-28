## 0x02. i18n
`Back-end`

### Resources
- Read or watch:

- [Flask-Babel](https://web.archive.org/web/20201111174034/https://flask-babel.tkte.ch/)
- [Flask i18n tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xiii-i18n-and-l10n)
- [pytz](https://pypi.org/project/pytz/)

Tasks
0. Basic Flask app
- First you will setup a basic Flask app in `0-app.py`. Create a single `/` route and an `index.html` template that simply outputs “Welcome to Holberton” as page title `(<title>)` and “Hello world” as header `(<h1>)`.
- File: `0-app.py, templates/0-index.html`

1. Basic Babel setup
- Install the Babel Flask extension:

`$ pip3 install flask_babel==2.0.0`
- Then instantiate the `Babel` object in your app. Store it in a module-level variable named `babel`.

- In order to configure available languages in our app, you will create a `Config` class that has a `LANGUAGES` class attribute equal to `["en", "fr"]`.

- Use `Config` to set Babel’s default locale `("en")` and timezone `("UTC")`.

- Use that class as config for your Flask app.
File: `1-app.py, templates/1-index.html`

2. Get locale from request
- Create a `get_locale` function with the `babel.localeselector` decorator. Use `request.accept_languages` to determine the best match with our supported languages.
- File: `2-app.py, templates/2-index.html`

3. Parametrize templates
- Use the `_` or `gettext` function to parametrize your templates. Use the message IDs `home_title` and `home_header`.

- Create a `babel.cfg` file containing
```
[python: **.py]
[jinja2: **/templates/**.html]
extensions=jinja2.ext.autoescape,jinja2.ext.with_
```
- Then initialize your translations with
```
$ pybabel extract -F babel.cfg -o messages.pot .
```
- and your two dictionaries with
```
$ pybabel init -i messages.pot -d translations -l en
$ pybabel init -i messages.pot -d translations -l fr
```
- Then edit files `translations/[en|fr]/LC_MESSAGES/messages.po` to provide the correct value for each message ID for each language. Use the following translations:


msgid			English						French
`home_title`	`"Welcome to Holberton"`	`"Bienvenue chez Holberton"`
`home_header`	`"Hello world!"`			`"Bonjour monde!"`
Then compile your dictionaries with
```
$ pybabel compile -d translations
```
- Reload the home page of your app and make sure that the correct messages show up.
File: `3-app.py, babel.cfg, templates/3-index.html, translations/en/LC_MESSAGES/messages.po, translations/fr/LC_MESSAGES/messages.po, translations/en/LC_MESSAGES/messages.mo, translations/fr/LC_MESSAGES/messages.mo`
