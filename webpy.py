import web

urls = (
        '/hello_1', 'hello_1',
        '/hello_2/(.*)', 'hello_2'
        )

app = web.application(urls, globals())
render = web.template.render('templates')


class hello:
    def GET(self, name):
        if not name:
            name = 'world'
        return 'hello,'+name


class hello_1:

    def GET(self):
        return render.index_1()


class hello_2:

    def GET(self, name):
        # name = "1111"
        return render.index_2(name)


if __name__ == "__main__":
    app.run()

