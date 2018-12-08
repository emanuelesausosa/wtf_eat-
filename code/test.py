from bottle import run, get, route


@route('/')
def index():
    # esto es un comentario
    return '<h1>Hello world<h1>'


if __name__ == '__main__':
    run(host='localhost', port=5000)
