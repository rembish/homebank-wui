from decimal import Decimal

from homebank.libraries.banking.gdate import from_gdate


class Transaction(object):
    def __init__(self, owner, tag):
        self.owner = owner

        self.amount = Decimal.from_float(float(tag.attrib["amount"]))
        self.account = next(
            x for x in self.owner.accounts if x.id == int(tag.attrib["account"])
        )
        self.mode_id = int(tag.attrib.get("paymode", 0))
        self.flags = int(tag.attrib.get("flags", 0)) or None
        self.payee_id = int(tag.attrib.get("payee", 0)) or None
        self.category_id = int(tag.attrib.get("category", 0)) or None

        self.wording = tag.attrib.get("wording")
        self.info = tag.attrib.get("info")

        self.date = from_gdate(int(tag.attrib["date"]))

        self.dst_account_id = int(tag.attrib.get("dst_account", 0)) or None

        self.id = None

    @property
    def payee(self):
        if not self.payee_id:
            return None
        return next(x for x in self.owner.payees if x.id == self.payee_id)

    @property
    def category(self):
        if not self.category_id:
            return None
        return next(
            x for x in self.owner.categories if x.id == self.category_id
        )

    @property
    def title(self):
        return self.info or self.wording or ""

    @property
    def mode(self):
        return {
            1: "ccard",
            2: "cheque",
            3: "cash",
            4: "transfer",
            5: "intransfer",
            6: "dcard",
            7: "standingorder",
            8: "epayment",
            9: "deposit",
            10: "fifee",
            11: "directdebit",
        }.get(self.mode_id, "none")

    @property
    def destination(self):
        if not self.dst_account_id:
            return None
        return next(
            x for x in self.owner.accounts if x.id == self.dst_account_id
        )
