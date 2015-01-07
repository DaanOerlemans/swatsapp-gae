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
    # The name of the user.
    name = ndb.StringProperty(required=True)

    # The device id of the user.
    device_id = ndb.StringProperty(required=True)

    # List of photos the user made.
    photos = ndb.KeyProperty(kind='Photo', repeated=True)

    # Timestamp of creation.
    created = ndb.DateTimeProperty(auto_now_add=True)


class Photo(ndb.Model):
    """
    Class to represent a photo.

    """
    image = ndb.BlobProperty()