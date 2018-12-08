import mysql.connector
from mysql.connector import errorcode


def add_new_companias(razon=None, marca=None):
    """insert data on companias table"""
    try:
        cnx = mysql.connector.connect(user="root", database="wtf_eat_db")
        cursor = cnx.cursor()

        """datos a almacenar"""
        company_info = {
            'razon': razon,
            'marca': marca
        }

        """creación del query"""
        query = ("INSERT INTO COMPANIAS"
                 "(RAZON_SOCIAL, NOMBRE_MARCA) "
                 "VALUES"
                 "("
                 "%(razon)s,"
                 "%(marca)s"
                 ")")
        cursor.execute(query, company_info)
        cnx.commit()
        cursor.close()
        cnx.close()

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Usuario / contraseña incorrecta")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("la base de datos no existe")
    else:
        cnx.close()


add_new_companias("Industrias Dinant", "Dinant")
