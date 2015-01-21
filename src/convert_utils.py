# encoding: utf-8

from __future__ import absolute_import
from __future__ import unicode_literals

from google.appengine.ext import ndb


def user_to_dict(user):
    """
    Convert a user object to dict format that can be returned through a
    json.dumps() response.

    Args:
        user: The user to convert to dict.

    Returns:
        The dict representation of the given user.

    """
    photos = ndb.get_multi(user.photos)
    return {
        'name': user.name,
        'device_id': user.device_id,
        'photos': [acc.key.id() for acc in photos],
        'id': user.key.id(),
        'created': user.created.strftime('%Y-%m-%dT%H:%M:%SZ')
    }


def photo_to_dict(photo, url):
    """
    Convert a photo object to dict format that can be returned through a
    json.dumps() response.

    Args:
        photo: The photo to convert to dict.
        url: The url to get the photo.

    Returns:
        The dict representation of the given photo.

    """
    return {
        'id':  photo.key.id(),
        'url': url,
        'created': photo.created.strftime('%Y-%m-%dT%H:%M:%SZ')
    }