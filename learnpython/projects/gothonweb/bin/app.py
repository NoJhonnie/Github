#coding=utf-8
import web
from gothonweb import map

web.config.debug = False

urls = (
  '/count', 'count',
  '/reset', 'reset'
)

app = web.application(urls, locals())
store = web.session.DiskStore('sessions')
session = web.session.Session(app, store, initializer={'count':0})
#render = web.template.render('templates/', base = "layout")

"""
index.html对应的内容
class Index(object):
    def GET(self):
        form = web.input(name="Nobody", greet=None)
        if form.greet:
            greeting = "%s, %s " % (form.greet, form.name)
            return render.index(greeting = greeting)
        else:
            return "ERROR:great is required."

class Index(object):
    def GET(self):
        return render.hello_form()
        
    def POST(self):
        form = web.input(name="Nobody", greet="Hola")
        greeting = "%s, %s" %(form.greet, form.name)
        return render.index(greeting = greeting)
"""
class count:
    def GET(self):
        session.count += 1
        return str(session.count)
        
class reset:
    def GET(self):
        session.kill()
        return ""


if __name__ == "__main__":
    app.run()