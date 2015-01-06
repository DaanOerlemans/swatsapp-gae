# encoding: utf-8

from __future__ import absolute_import
from __future__ import unicode_literals

from google.appengine.ext import ndb
"""
Models inherit from ndb.Model so
we can treat it as an entity which is useful when we want to
store it in the datastore.

"""


class User(ndb.Model):
    """
    Class to represent a user.

    """
    # The phone number of the user.
    phonenumber = ndb.StringProperty(required=True)

    # The email address of the user.
    email = ndb.StringProperty(required=True)

    # The password of the user, encrypted.
    password = ndb.StringProperty(required=True)

    # Timestamp of creation.
    created = ndb.DateTimeProperty(auto_now_add=True)
