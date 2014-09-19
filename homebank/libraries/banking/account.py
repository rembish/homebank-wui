from decimal import Decimal


class Account(object):
    def __init__(self, owner, tag):
        self.owner = owner
        self.id = int(tag.attrib["key"])
        self.type = int(tag.attrib["type"])
        self.name = tag.attrib["name"]
        self.flags = int(tag.attrib.get("flags", 0))

        self._initial = Decimal.from_float(float(tag.attrib["initial"]))

    @property
    def balance(self):
        return self._initial + sum(x.amount for x in self.transactions)

    @property
    def transactions(self):
        return filter(lambda x: x.account == self, self.owner.transactions)

    @property
    def hidden(self):
        return self.flags & 16

    def __str__(self):
        return self.name
