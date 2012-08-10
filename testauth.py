#-*- coding: utf-8 -*-
import urllib,urllib2
from weibo  import APIClient

#APP_KEY = "3302956248"
#APP_SECRET="a3d8968cc21fd8115ad6e90994755cfc"
APP_KEY = "202088835"
APP_SECRET="9567e3782151dcfd1a9bd2dd099d957f"
CALLBACK_URL = "https://api.weibo.com/oauth2/default.html"
#CALLBACK_URL = "http://me.cloudaice.com"
#CALLBACK_URL = "http://www.baidu.com"

DOMAIN = "http://api.t.sina.com.cn/oauth/access_token"
client = APIClient(app_key = APP_KEY,app_secret = APP_SECRET,redirect_uri = CALLBACK_URL)
url = client.get_authorize_url(redirect_uri = CALLBACK_URL)
#print url
import webbrowser

webbrowser.open(url)
code = raw_input("input code: ")
#access_token = "2.00FvIAQCsnrWbD4018a02070fVoPjD"



