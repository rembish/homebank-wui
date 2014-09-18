from flask import request, render_template
from functools import wraps


def with_template(template=None):
    def proxy(function):
        @wraps(function)
        def decorator(*args, **kwargs):
            template_name = template
            if not template_name:
                template_name = '%s.html' % request.endpoint.replace('.', '/')

            context = function(*args, **kwargs) or {}
            if not isinstance(context, dict):
                return context

            return render_template(template_name, **context)
        return decorator

    if callable(template):  # @with_template call
        function = template
        template = None
        return proxy(function)

    return proxy  # @with_template(...) call
