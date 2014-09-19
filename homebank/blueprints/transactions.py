from flask.ext.login import login_required

from homebank.libraries.decorators import with_template
from homebank.libraries.flask_ext import Blueprint


root = Blueprint('transactions', __name__)

@root.route("/transaction/new")
@root.route("/transaction/<int:id>")
@with_template
@login_required
def edit(id=None):
    pass

