import mysql.connector
from mysql.connector import errorcode

cnx = None


def conectar():
    try:
        cnx = mysql.connector.connect(user='root', database='wtf_eat_db')
        print("conexion exitosa!")
        cursor = cnx.cursor()
        return cursor

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Something is wrong with your user name or password')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print('Database does not exist')
        else:
            print(err)


def cerrar():
    print('ha finalizado la transaccion, cerrando conexion...')
    cnx.close()


def get_companias():
    cursor = conectar()
    query = (
        "select c.RAZON_SOCIAL as razon, c.NOMBRE_MARCA as marca from companias c;")
    cursor.execute(query)

    data = []

    for(razon, marca) in cursor:
        data.append({
            'razonSocial': razon,
            'marca': marca
        })

    print(data)
    cerrar()


if __name__ == "__main__":
    get_companias()
