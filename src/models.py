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
    # The photo image
    image = ndb.BlobProperty(default=None)

    # Timestamp of creation.
    created = ndb.DateTimeProperty(auto_now_add=True)


class News(ndb.Model):
    """
    Class to represent a news item.

    """
    # The poster of the news item.
    poster = ndb.StringProperty(required=True)

    # The poster of the news item.
    poster_profile_picture = ndb.StringProperty(required=True)

    # The message of the news item.
    message = ndb.StringProperty(required=True)

    # The image url posted with the news item
    image_url = ndb.StringProperty()

    # Timestamp of creation.
    created = ndb.DateTimeProperty(auto_now_add=True)