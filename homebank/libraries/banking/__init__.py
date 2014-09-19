from werkzeug.utils import cached_property
from xml.etree.ElementTree import parse

from homebank.libraries.banking.account import Account
from homebank.libraries.banking.category import Category
from homebank.libraries.banking.payee import Payee
from homebank.libraries.banking.transaction import Transaction


class Banking(object):
    def __init__(self, filename):
        self.tree = parse(filename)
        self.root = self.tree.getroot()

    def _get_list(self, predicate, cls):
        data = []
        for x in self.root.iter(predicate):
            data.append(cls(self, x))
        return data

    @cached_property
    def accounts(self):
        return self._get_list("account", Account)

    @property
    def transactions(self):
        data = self._get_list("ope", Transaction)
        for i, t in enumerate(data):
            t.id = i
        return data

    @property
    def categories(self):
        return self._get_list("cat", Category)

    @property
    def payees(self):
        return self._get_list("pay", Payee)
