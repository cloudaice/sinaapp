from weibo import APIClient

APP_KEY = '3302956248' #app key
APP_SECRET = 'a3d8968cc21fd8115ad6e90994755cfc' #app secret
CALLBACK_URL = 'http://me.cloudaice.com/callback' #callback

client = APIClient(app_key=APP_KEY,app_secret = APP_SECRET,redirect_url=CALLBACK_URL)
url = client.get_authorize_url()
