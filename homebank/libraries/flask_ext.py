from flask import Blueprint as BaseBlueprint, current_app
from flask.ext.login import UserMixin

from homebank.libraries.banking import Banking

__all__ = ['Blueprint']


class Blueprint(BaseBlueprint):
    def __init__(self, name, import_name, **kwargs):
        kwargs.setdefault("template_folder", "templates")
        super(Blueprint, self).__init__(name, import_name, **kwargs)


class User(UserMixin):
    def get_id(self):
        return current_app.config['SECRET_KEY']


def get_banking():
    if "XHB_INSTANCE" not in current_app.config:
        current_app.config['XHB_INSTANCE'] = Banking(current_app.config['XHB'])
    return current_app.config['XHB_INSTANCE']
