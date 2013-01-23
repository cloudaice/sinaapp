import	web
from sina import *
import string

urls = (
   '/','index',
   '/getFanNumber','getFanNumber',
   '/getFanList','getFanList',
   '/getLastWeiboId','getLastWeiboId',
   '/getWeiboInfoByTime','getWeiboInfoByTime'
   )

app = web.application(urls,globals())


class index:
	def GET(self):
		fd = open('index.html','r')
		return fd.read()

class getFanList:
    def POST(self):
        req_data = web.input()
        user_id = req_data.user_id
        return  get_fans_id(user_id)

class getFanNumber:
    def POST(self):
        return 'hello'

class getLastWeiboId:
    def POST(self):
        req_data = web.input()
        weibo_id = req_data.user_id.strip()
        return get_last_weibo_id(weibo_id)

class getWeiboInfoByTime:
    def POST(self):
        req_data = web.input()
        user_id = req_data.user_id.strip()
        weibo_id = req_data.weibo_id.strip()
        return get_weibo_ids_since(user_id,weibo_id)


if __name__ == "__main__":
	app.run()
