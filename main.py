# encoding: utf-8

from __future__ import absolute_import
from __future__ import unicode_literals

import webapp2
from webapp2_extras.routes import RedirectRoute

import api_urls
from src.pl import handlers
from src.bll import services
from src.dal import repositories

# Overriding default routes.
handlers = [
    (api_urls.USER, handlers.UserHandler),
    (api_urls.USERS, handlers.UsersHandler),
    (api_urls.PHOTO, handlers.PhotoHandler),
    (api_urls.PHOTOS, handlers.PhotosHandler),
    (api_urls.NEWS_ITEMS, handlers.NewsItemsHandler),
    (api_urls.NEWS_ITEM, handlers.NewsItemHandler)
]

routes = [RedirectRoute(url, handler, url, strict_slash=True)
          for url, handler in handlers]

# WSGI application configuration.
config = {'sa': {}}

# Manage service class dependency injection.
config['sa']['user_service'] = services.UserService(
    repositories.UserRepository()
)
config['sa']['photo_service'] = services.PhotoService(
    repositories.PhotoRepository()
)
config['sa']['news_item_service'] = services.NewsItemService(
    repositories.NewsItemRepository()
)


class SwatsAppWSGIApplication(webapp2.WSGIApplication):
    """
    WSGI application for the SwatsApp API.

    """
    allowed_methods = frozenset(('GET', 'POST', 'HEAD', 'OPTIONS', 'PUT',
                                 'DELETE', 'TRACE', 'PATCH'))


def get_application(routes_, config_):
    return SwatsAppWSGIApplication(debug=False, routes=routes_, config=config_)

application = get_application(routes, config)
