from bottle import run, get, post, route, request
import mysql.connector
from mysql.connector import errorcode


@route('/')
def index():
    # esto es un comentario
    return '<h1>Hello world<h1>'


@get('/api/companias/')
def get_companias():
    try:
        cnx = mysql.connector.connect(user='root', database='wtf_eat_db')
        cursor = cnx.cursor()

        query = (
            "select c.RAZON_SOCIAL as razon, c.NOMBRE_MARCA as marca from companias c;")
        cursor.execute(query)

        data = []

        for(razon, marca) in cursor:
            data.append({
                'razonSocial': razon,
                'marca': marca
            })
        return {'data': data}
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            return {'data': 'Something is wrong with your user name or password'}
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            return {'data': 'Database does not exist'}
        else:
            print(err)
    else:
        cnx.close()


@post('/api/companias/add')
def add_new_companias():
    username = request.form.get('username')
    print(**username)


if __name__ == '__main__':
    run(host='localhost', port=5000, reloader=True)
