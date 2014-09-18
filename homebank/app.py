from logging import StreamHandler, WARNING, Formatter
from logging.handlers import WatchedFileHandler
from flask.app import Flask
from flask.ext.login import LoginManager
from flask.templating import render_template
from werkzeug.utils import import_string

from homebank.libraries.flask_ext import User


def make_app(import_name=__name__,
             config='homebank.settings.Configuration',
             debug=False):

    app = Flask(import_name)
    app.config.from_object(config)
    app.config.from_envvar('FLASK_SETTINGS', silent=True)
    app.debug = debug
    app.jinja_env.filters['currency'] = \
        lambda x: "{:,.2f} %s".format(x).replace(",", " ").replace(".", ",") % (
            app.config.get('CURRENCY', '')
        )

    if app.debug:
        import_string('flask.ext.debugtoolbar:DebugToolbarExtension')(app)

    @app.errorhandler(404)
    def not_found(ex):
        return render_template("404.html"), 404

    for blueprint in ['__init__', 'dashboard']:
        app.register_blueprint(import_string(
            'homebank.blueprints.%s:root' % blueprint))

    login_manager = LoginManager(app=app)
    login_manager.login_view = "index.login"
    login_manager.session_protection = "strong"

    @login_manager.user_loader
    def load_user(uid):
        if uid != app.config['SECRET_KEY']:
            return None
        return User()

    if not app.debug:
        handler = StreamHandler()
        if 'ERROR_LOG' in app.config:
            handler = WatchedFileHandler(app.config['ERROR_LOG'])

        handler.setLevel(WARNING)
        handler.setFormatter(Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
        app.logger.addHandler(handler)

    return app
