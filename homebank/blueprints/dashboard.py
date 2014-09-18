from flask.ext.login import login_required

from homebank.libraries.decorators import with_template
from homebank.libraries.flask_ext import Blueprint, get_banking


root = Blueprint('dashboard', __name__)


@root.route("/dashboard")
@root.route("/dashboard/accounts")
@with_template
@login_required
def accounts():
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
