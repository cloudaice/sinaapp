# -*- coding: utf-8 -*-
from weibo import APIClient

APP_KEY = "3302956248"
APP_SECRET="a3d8968cc21fd8115ad6e90994755cfc"
CALLBACK_URL = "https://api.weibo.com/oauth2/default.html"
client = APIClient(app_key = APP_KEY, app_secret = APP_SECRET, redirect_uri = CALLBACK_URL)
url = client.get_authorize_url()
print url
