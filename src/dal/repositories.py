# encoding: utf-8

from __future__ import absolute_import
from __future__ import unicode_literals

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