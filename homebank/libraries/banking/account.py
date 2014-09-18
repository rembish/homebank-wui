from decimal import Decimal


class Account(object):
    def __init__(self, root, tag):
        self.root = root
        self.id = int(tag.attrib["key"])
        self.type = int(tag.attrib["type"])
        self.name = tag.attrib["name"]
        self.flags = int(tag.attrib.get("flags", 0))

        self._initial = Decimal.from_float(float(tag.attrib["initial"]))
        self._delta = None

    @property
    def balance(self):
        return self._initial + self.delta

    @property
    def delta(self):
        if self._delta is None:
            self._delta = Decimal()
            predicate = ".//ope[@account='%d']" % self.id
            for operation in self.root.findall(predicate):
                self._delta += Decimal.from_float(float(
                    operation.attrib["amount"]))

            self._delta = self._delta or None

        return self._delta or 0

    @property
    def hidden(self):
        return self.flags & 16
