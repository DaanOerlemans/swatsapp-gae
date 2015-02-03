# encoding: utf-8

from __future__ import absolute_import
from __future__ import unicode_literals


class DuplicateEntity(Exception):
    """
    Exception to raise when trying to create a duplicate entity.

    """


class NotFoundEntity(Exception):
    """
    Exception to raise when trying to create a not found entity.

    """