# encoding: utf-8

from __future__ import absolute_import
from __future__ import unicode_literals


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

    def get_by_id(self, user_id):
        """
        Find a user by its unique id.

        Args:
            user_id: The id to get the user.

        Returns:
            The user if it was found, or None if it was not.

        """
        return self.user_repo.get_by_id(user_id)


class PhotoService(object):
    """
    Service class that connects the presentation layer to the domain.

    """
    def __init__(self, photo_repo):
        """
        Create a new instance.

        Args:
            photo_repo: The PhotoRepository to use.

        """
        self.photo_repo = photo_repo

    def create(self, photo, user):
        """
        Creates a new photo by calling the photo repository.

        Args:
            photo: The photo to create.
            user: The user to assign the photo to.

        Returns:
            The created photo.

        """
        return self.photo_repo.create(photo, user)


class NewsItemService(object):
    """
    Service class that connects the presentation layer to the domain.

    """
    def __init__(self, news_repo):
        """
        Create a new instance.

        Args:
            news_repo: The NewsRepository to use.

        """
        self.news_repo = news_repo

    def create(self, news):
        """
        Creates a new photo by calling the photo repository.

        Args:
            news: The news to create.

        Returns:
            The created news.

        """
        return self.news_repo.create(news)