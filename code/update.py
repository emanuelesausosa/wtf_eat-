import mysql.connector as conn

db_credentials = {
    'user': 'root',
    'database': 'wtf_eat_db'
}


def update_nombre_marca(marca_actual=None, marca_nuevo=None):
    """método que actualiza el nombre de la marca"""
    try:
        cnx = conn.connect(user="root", database="wtf_eat_db")
        cursor = cnx.cursor()

        data = {
            'nuevo': marca_nuevo,
            'actual': marca_actual
        }

        query = ("UPDATE COMPANIAS"
                 " SET NOMBRE_MARCA=%(nuevo)s"
                 " WHERE NOMBRE_MARCA=%(actual)s")
        cursor.execute(query, data)

        cnx.commit()
        cursor.close()
        cnx.close()

    except conn.Error:
        print("ha ocurrido un error al hacer la consulta")
        return
    else:
        cnx.close()


update_nombre_marca("Zambos", "Caribe")
