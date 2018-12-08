import mysql.connector as conn
from mysql.connector import errorcode


def get_all_companias():
    """método para obtener todas las companias"""

    """creo la conexión"""
    try:
        cnx = conn.connect(user="root", database="wtf_eat_db")
        cursor = cnx.cursor()

        query = (
            "SELECT C.RAZON_SOCIAL AS razon, C.NOMBRE_MARCA AS marca FROM COMPANIAS C;")
        cursor.execute(query)

        for(razon, marca) in cursor:
            print("{} - {}".format(razon, marca))

        cursor.close()  # se cierra el cursor
        cnx.close()  # """se cierra la conexón cnx"""

    except conn.Error:
        return
    else:
        cnx.close()


def get_compania_by_marca(marca=None):
    """devuelve las companias por el nombre de la marca"""
    try:
        cnx = conn.connect(user="root", database="wtf_eat_db")
        cursor = cnx.cursor()

        query = (
            "SELECT C.RAZON_SOCIAL AS razon, C.NOMBRE_MARCA AS marca FROM COMPANIAS C WHERE C.NOMBRE_MARCA='{}';".format(marca))
        cursor.execute(query)

        for(razon, marca) in cursor:
            print("{} - {}".format(razon, marca))

        cursor.close()  # se cierra el cursor
        cnx.close()  # """se cierra la conexón cnx"""

    except conn.Error:
        return
    else:
        cnx.close()


# get_all_companias()
get_compania_by_marca("Zambos")
