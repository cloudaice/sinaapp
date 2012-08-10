import	web

urls = (
   '/','index',
   '/result1','result1',
   '/result2','result2'
   )

app = web.application(urls,globals())


class index:
	def GET(self):
		fd = open('index.html','r')
		return fd.read()

class result1:

    def GET(self):
        return "get1"

	def POST(self):
		return "result1"

class result2:
    def POST(self):
        return "result2"

if __name__ == "__main__":
	app.run()
