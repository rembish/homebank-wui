class Payee(object):
    def __init__(self, owner, tag):
        self.owner = owner
        self.id = int(tag.attrib["key"])
        self.name = tag.attrib["name"]

    def __str__(self):
        return self.name
