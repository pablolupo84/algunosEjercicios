import mysql.connector
from mysql.connector import errorcode

class Conexion:
    def conectar(self):
        try:
            conexion = mysql.connector.connect(user='root',password='root',host='localhost',database='app_workana')
            print("conectado correctamente")
            return conexion
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Error al conectar")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Base de datos no existente")
            else:
                print(err)
            return None
    def CerrarConexion(self,conexion):
        print("Cerrando conexion...")
        conexion.close()
        print("Conexion cerrada")
        

