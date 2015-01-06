# encoding: utf-8

from __future__ import absolute_import
from __future__ import unicode_literals

USERS = '/users'
USER = USERS + '/<user_id>'

NEWS = '/news'
TWITTER = '/twitter'

PHOTOS = USER + '/photos'
PHOTO = PHOTOS + '/<photo_id>'

PUSH_NOTIFICATION = '/push'