﻿#coding=utf-8
import web

urls = (
  '/hello', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/', base = "layout")

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
"""
class Index(object):
    def GET(self):
        return render.hello_form()
        
    def POST(self):
        form = web.input(name="Nobody", greet="Hola")
        greeting = "%s, %s" %(form.greet, form.name)
        return render.index(greeting = greeting)


if __name__ == "__main__":
    app.run()