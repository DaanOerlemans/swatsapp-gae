# encoding: utf-8

from __future__ import absolute_import
from __future__ import unicode_literals

USERS = '/users'
USER = USERS + '/<user_id>'

NEWS_ITEM = '/news_item'
NEWS_ITEMS = '/news_items'

PHOTOS = USER + '/photos'
PHOTO = PHOTOS + '/<photo_id>'

PUSH_NOTIFICATION = USER + '/push'