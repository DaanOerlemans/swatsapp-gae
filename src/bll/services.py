# encoding: utf-8

from __future__ import absolute_import
from __future__ import unicode_literals

from src import exc


class UserService(object):
    """
    Service class that connects the presentation layer to the domain.

    """
    def __init__(self, user_repo):
        """
        Create a new instance.

        Args:
            user_repo: The UserRepository to use.

        """
        self.user_repo = user_repo

    def create(self, user):
        """
        Creates a new user by calling the user repository.

        Args:
            user: The user to create.

        Returns:
            The created user.

        """
        return self.user_repo.create(user)