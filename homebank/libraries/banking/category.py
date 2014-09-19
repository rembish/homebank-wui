class Category(object):
    def __init__(self, owner, tag):
        self.owner = owner
        self.id = int(tag.attrib["key"])
        self.parent_id = int(tag.attrib.get("parent", 0)) or None
        self.flags = int(tag.attrib.get("flags", 0)) or None
        self.name = tag.attrib["name"]

    @property
    def parent(self):
        if self.parent_id:
            return next(
                x for x in self.owner.categories if x.id == self.parent_id
            )
        return None

    @property
    def fullname(self):
        current = self
        chunks = []

        while current:
            chunks = [current.name] + chunks
            current = current.parent

        return ":".join(chunks)

    def __str__(self):
        return self.fullname
