# encoding: utf-8

from __future__ import absolute_import
from __future__ import unicode_literals

import httplib
import json


def decorator_with_args(decorator):
    """
    Decorator to decorate a decorator so it can pass args.

    Args:
        decorator: The decorator to decorate.

    Returns:
        A modified decorator, wrapped in another decorator.

    """
    def decorator_maker(*args, **kwargs):
        def decorator_wrapper(func):
            return decorator(func, *args, **kwargs)
        return decorator_wrapper
    return decorator_maker


@decorator_with_args
def accepts(f, *args, **kwargs):
    """
    Decorator that checks the content type of a request passed to a requesthandler's function.

    Args:
        f: The function to decorate.
        args: The args that are passed through the decorator.
        kwargs: The kwargs that are passed through the decorator.

        Example: accepts('json', 'xml', block=True) --> args: ('json', 'xml',) - kwargs: {'block': True}

    Returns:
        The function, wrapper in a decorator.

    """
    def wrapper(*function_args, **function_kwargs):
        selfy = function_args[0]

        if not selfy.request.headers['Content-Type'] in args:
            selfy.response.set_status(httplib.UNSUPPORTED_MEDIA_TYPE)
            selfy.response.headers[str('Content-Type')] = (str('application/json'))
            selfy.response.out.write(json.dumps({
                'error': 'Supported Content-Types: %s' % (
                    ", ".join([ct for ct in args])
                )
            }))
            return

        try:
            request_body = json.loads(selfy.request.body)
            function_args = function_args + (request_body,)
        except ValueError:
            selfy.response.set_status(httplib.BAD_REQUEST)
            selfy.response.headers[str('Content-Type')] = (str('application/json'))
            selfy.response.out.write(json.dumps({
                'error': 'Something went wrong while parsing the JSON data '
                         'please verify that it\'s correct.'
            }))
            return

        return f(*function_args, **function_kwargs)
    return wrapper


@decorator_with_args
def returns(f, content_type, *args, **kwargs):
    """
    Decorator that formats the output of the decorated function to the given format.

    Args:
        f: The function to decorate.
        content_type: The Content-Type that should be set for the response.
            The response body should be formatted accordingly.
        args: The args that are passed through the decorator.
        kwargs: The kwargs that are passed through the decorator.

        Example: returns('json') --> args: ('json',) - kwargs: {}

    Returns:
        The function, wrapper in a decorator.

    Note:
        In order for this decorator to function properly, the return data of the
            decorated function should be as follows:
            A tuple (<statuscode>, <message>) where message is:
            - For JSON: a list (collection) or a dict (single object).

        A DELETE function returns no content and therefore only returns a status
            code. In that case result is not a tuple but just an int.

    """
    def wrapper(*function_args, **function_kwargs):
        selfy = function_args[0]

        # Call the decorated function and handle the response.
        result = f(*function_args, **function_kwargs)

        if isinstance(result, int):
            # f is a DELETE handler and returned only an int.
            status_code = result
            selfy.response.set_status(status_code)
            selfy.response.headers[str('Content-Type')] = (str('text/plain'))
            return

        status_code = result[0]
        selfy.response.set_status(status_code)

        response_dict = result[1]
        if content_type == 'application/json':
            selfy.response.headers[str('Content-Type')] = (str('application/json'))
            selfy.response.out.write(json.dumps(response_dict))
        else:
            selfy.response.headers[str('Content-Type')] = (str('text/plain'))
            selfy.response.out.write(str(response_dict))
        return
    return wrapper


@decorator_with_args
def json_requires_fields(f, *args, **kwargs):
    """
    Decorator that checks if the request that is passed to a function has
    a body that contains all of the required fields.

    Args:
        f: The function to decorate.
        args: The args that are passed through the decorator.
        kwargs: The kwargs that are passed through the decorator.

        Example: requires('name', 'password', block=True)
            --> args: ('name', 'password',) - kwargs: {'block': True}

    Returns:
        The function, wrapper in a decorator.

    """
    def wrapper(*function_args, **function_kwargs):
        selfy = function_args[0]

        # Check if the request is valid JSON.
        request = {}
        try:
            request = json.loads(selfy.request.body)
        except ValueError:
            selfy.response.set_status(httplib.BAD_REQUEST)
            selfy.response.out.write(json.dumps({
                'error': 'Something went wrong while parsing the JSON data '
                         'please verify that it\'s correct.'
            }))
            return

        errors = {'error': []}
        for field in args:
            if not field in request:
                errors['error'].append({
                    'missing_field': field
                })

        either = kwargs.get('either')
        if either:
            if all(field in request for field in either):
                errors['error'].append({
                    'excess_field': '%s or %s' % (tuple(either))
                })
            if not any(field in request for field in either):
                errors['error'].append({
                    'missing_field': '%s or %s' % (tuple(either))
                })

        if errors['error']:
            selfy.response.set_status(httplib.UNPROCESSABLE_ENTITY)
            selfy.response.headers[str('Content-Type')] = (str('application/json'))
            selfy.response.out.write(json.dumps(errors))
            return

        return f(*function_args, **function_kwargs)
    return wrapper
