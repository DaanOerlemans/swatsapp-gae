from __future__ import absolute_import
from __future__ import unicode_literals

import httplib

import webapp2

import api_urls
from src import models
from src import exc
from src.decorators import accepts
from src.decorators import returns
from src.decorators import json_requires_fields
from src import convert_utils


class UserHandler(webapp2.RequestHandler):
    """
    Serves as base class for UsersHandler.

    """
    user_service = None

    def initialize(self, request, response):
        """
        Initialize the handler and fetch the required services from
        the current WSGI application's config.

        """
        webapp2.RequestHandler.initialize(self, request, response)
        services = ['user_service']
        config = self.app.config.load_config('sa', required_keys=services)
        self.user_service = config['user_service']


class UsersHandler(UserHandler):
    """
    Handler for creating new users.

    """
    url = api_urls.USERS

    @accepts('application/json')
    @json_requires_fields('name', 'device_id')
    @returns('application/json')
    def post(self, request):
        """
        Create a new user.

        Keyword Args (via the request object):
            phonenumber: The phonenumber of the user.
            email: The email address of the user.
            password: The password of the user, encrypted.

        Returns:
            201 Ok and the created user as JSON: If the request is valid and
                creation was successful.
            409 Conflict: If the user already exists in the database.
            422 Unprocessable Entity and an error message: If the request is
                invalid.

        """
        # Build a User object from the kwargs.
        # Required parameters.
        user = models.User(
            name=request['name'],
            device_id=request['device_id'],
            photos=[]
        )

        try:
            user = self.user_service.create(user)
        except exc.DuplicateEntity:
            return httplib.CONFLICT, {
                'error': 'There already is an account for this device_id {}'.format(user.device_id)
                }

        # If the user is created successfully.
        return httplib.CREATED, convert_utils.user_to_dict(user)