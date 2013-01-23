#!/usr/bin/env python
# -*- coding: utf8 -*-
from weibo2 import *

if __name__ == "__main__":
    APP_KEY = '3465300940'
    APP_SECRET = 'eef08cc03700d208f793605541e03807'
    CALLBACK_URL = 'https://api.weibo.com/oauth2/default.html'
    USERID = '2068721331'
    PASSWD = "1'p'2'c'"

    client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
    if client.imitateLogin(USERID,PASSWD):
        print client.access_token,client.expires_in
        print "auth ok"
    else:
        print 'error'


