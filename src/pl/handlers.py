from __future__ import absolute_import
from __future__ import unicode_literals

import httplib

import webapp2
import oauth2 as oauth
import json

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


class NewsItemHandler(webapp2.RequestHandler):
    """
    Serves as base class for NewsItemsHandler.

    """
    url = api_urls.NEWS

    news_item_service = None

    def initialize(self, request, response):
        """
        Initialize the handler and fetch the required services from
        the current WSGI application's config.

        """
        webapp2.RequestHandler.initialize(self, request, response)
        services = ['news_item_service']
        config = self.app.config.load_config('sa', required_keys=services)
        self.news_item_service = config['news_item_service']

    @returns('application/json')
    def get(self):
        """
        Retrieve all news for a user.

        Args:
            user_id: The id of user to retrieve the news for.

        Returns:
            200 Ok and the JSON representation of all news for the user.
            404 Not Found: If the user was not found.

        """
        consumer = oauth.Consumer(key="z0oq1oiNDWC1x6jDHpYiVYhFD", secret="hfPuWcPf48XfhkfhaKs4jGFGNqgezCGUiJ0YEggjT03AWMALcX")
        token = oauth.Token(key="2990304898-hZ9gmp9YoQdnKuPQJNYeDgc7tea9HztPUnn43YM", secret="J1tahrQahs7966LzqXvTH5ch9jHFVsLnuVPyMz22JzwhH")
        client = oauth.Client(consumer, token)
        urls = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=vcdeswatsers"
        resp, content = client.request(urls)

        news_items = []
        decoded_twitter_stream = json.loads(content)
        for tweet in decoded_twitter_stream:
            user = tweet['user']['screen_name']
            profile_image = tweet['user']['profile_image_url']
            if 'retweeted_status' in tweet:
                retweet_item = tweet['retweeted_status']
                user = retweet_item['user']['screen_name']
                profile_image = retweet_item['user']['profile_image_url']
            news_item = models.News(
                poster=user,
                poster_profile_picture=profile_image,
                message=tweet['text']
            )
            if 'media' in tweet['entities']:
                news_item.image_url = tweet['entities']['media'][0]['media_url']
            news_items.append(news_item)

        return httplib.OK, [convert_utils.news_to_dict(news_item) for news_item in news_items]
