from flask.globals import current_app

from homebank.libraries.decorators import with_template
from homebank.libraries.flask_ext import Blueprint


root = Blueprint('index', __name__)


@root.route("/")
@with_template("index.html")
def index():
    pass


@root.route('/favicon.ico')
def favicon():
    return send_from_directory(
        current_app.static_folder, 'favicon.ico', mimetype='image/x-icon')

