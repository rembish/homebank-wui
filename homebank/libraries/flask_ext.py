from flask import Blueprint as BaseBlueprint, Flask

__all__ = ['Blueprint']


class Blueprint(BaseBlueprint):
    def __init__(self, name, import_name, **kwargs):
        kwargs.setdefault("template_folder", "templates")
        super(Blueprint, self).__init__(name, import_name, **kwargs)
