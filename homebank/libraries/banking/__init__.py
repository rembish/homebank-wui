from werkzeug.utils import cached_property
from xml.etree.ElementTree import parse

from homebank.libraries.banking.account import Account


class Banking(object):
    def __init__(self, filename):
        self.tree = parse(filename)
        self.root = self.tree.getroot()

    @cached_property
    def accounts(self):
        data = []
        for acc in self.root.iter("account"):
            data.append(Account(self.root, acc))
        return data
