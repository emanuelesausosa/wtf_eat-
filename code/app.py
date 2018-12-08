from bottle import run, request, route, get, post


@route('/')
def index():
    return '<h1>Hello world 2<h1>'


@get('/api/companias')
def companias_index():
    return {'data': 'estas son las companias'}


@get('/api/companias/<marca>')
def get_companias_marca(marca=None):
    data = marca
    return {'data': data}


@post('/api/companias/new')
def add_new_compania():
    data = request.json.get('name')
    return {'data': data}


if __name__ == '__main__':
    run(host='127.0.0.1', port=5000, reloader=True)
