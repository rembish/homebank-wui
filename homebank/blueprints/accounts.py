from flask.ext.login import login_required

from homebank.libraries.decorators import with_template
from homebank.libraries.flask_ext import Blueprint, get_banking


root = Blueprint('accounts', __name__)


@root.route("/accounts")
@with_template
@login_required
def index():
    banking = get_banking()
    return {
        "accounts": banking.accounts,
        "account_types": {
            1: "Cash",
            2: "Bank",
            3: "Asset",
            4: "Credit card",
            5: "Liability",
        }
    }


@root.route("/accounts/<int:id>")
@with_template
@login_required
def view(id):
    banking = get_banking()
    return {
        "account": next(x for x in banking.accounts if x.id == id),
    }
