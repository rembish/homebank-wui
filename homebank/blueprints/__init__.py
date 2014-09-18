from flask.ext.login import login_required, login_user, logout_user
from flask.globals import current_app, request
from flask.helpers import send_from_directory, url_for
from werkzeug.utils import redirect

from homebank.libraries.decorators import with_template
from homebank.libraries.flask_ext import Blueprint, User


root = Blueprint('index', __name__)


@root.route("/")
@login_required
def index():
    return redirect(url_for("dashboard.accounts"))


@root.route("/login", methods=("POST", "GET"))
@with_template("login.html")
def login():
    secret = request.form.get("secret", None)
    if secret == current_app.config['SECRET_KEY']:
        login_user(User())
        return redirect(request.form.get("next") or url_for("index.index"))

    return {
        "next": request.form.get("next")
    }

@root.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index.index"))

@root.route('/favicon.ico')
@root.route('/<png>.png')
def favicon(png=None):
    icon = "%s.png" % png if png else "favicon.ico"
    mime = "png" if png else "x-icon"
    return send_from_directory(
        "%s/img/" % current_app.static_folder, icon, mimetype='image/%s' % mime)

