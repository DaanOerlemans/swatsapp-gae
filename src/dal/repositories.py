# encoding: utf-8

from __future__ import absolute_import
from __future__ import unicode_literals

from google.appengine.ext import ndb

from src import models
from src import exc


class UserRepository(object):
    """
    Repository that handles storage and retrieval of models.User objects
    in and from the datastore.

    """
    def create(self, user):
        """
        Create the given user in the datastore if it doesn't exist yet.

        Args:
            user: The user to create.

        Returns:
            The created user.

        Raises:
            exc.DuplicateEntity: If the desired username is
                already taken.

        """
        duplicate_user = models.User.query(models.User.device_id == user.device_id).fetch()
        if duplicate_user:
            raise exc.DuplicateEntity()

        user.put()
        return user

    def get_by_id(self, user_id):
        """
        Find a user by its unique id.

        Args:
            user_id: The id to find the user for.

        Returns:
            The user if it was found, or None if it was not.

        """
        user = models.User.get_by_id(user_id)
        if not user:
            raise exc.NotFoundEntity()
        return user


class PhotoRepository(object):
    """
    Repository that handles storage and retrieval of models.Photo objects
    in and from the datastore.

    """
    def create(self, photo, user):
        """
        Create the given photo in the datastore if it doesn't exist yet.

        Args:
            photo: The photo to create.
            user: The user to assign the photo to.

        Returns:
            The created photo.

        """
        photo.put()
        user.photos.append(photo.key)
        user.put()
        return photo

    def get_by_id(self, photo_id):
        """
        Find a user by its unique id.

        Args:
            user_id: The id to find the user for.

        Returns:
            The user if it was found, or None if it was not.

        """
        photo = models.Photo.get_by_id(photo_id)
        if not photo:
            raise exc.NotFoundEntity()
        return photo


class NewsItemRepository(object):
    """
    Repository that handles storage and retrieval of models.News objects
    in and from the datastore.

    """
    def create(self, news):
        """
        Create the given photo in the datastore if it doesn't exist yet.

        Args:
            news: The news to create.

        Returns:
            The created news.

        """
        news.put()
        return news