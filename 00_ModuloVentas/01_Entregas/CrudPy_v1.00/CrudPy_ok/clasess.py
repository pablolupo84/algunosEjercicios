from conexion import *

class Articulos(Conexion):
    
    def insertar(self,d,c,s,pv):
        cnx=self.conectar()
        cursor = cnx.cursor()
        cursor.execute("INSERT INTO articulos VALUES(null,'"+d+"','"+c+"','"+s+"','"+pv+"',null)")
        cnx.commit()
        self.CerrarConexion(cnx)

    def cargar(self,id_articulo):
        cnx=self.conectar()
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM articulos WHERE id_articulo="+str(id_articulo))
        arreglo = []
        for articulo in cursor:
            arreglo.append(articulo)
        self.CerrarConexion(cnx)
        return arreglo

    def modificar(self,d,c,s,pv,id_articulo):
        cnx = self.conectar()
        cursor = cnx.cursor()
        cursor.execute("UPDATE articulos SET descripcion='"+d+"',codigo='"+c+"',stock='"+s+"',precio_vta='"+pv+"' WHERE id_articulo='"+str(id_articulo)+"'")
        cnx.commit()
        self.CerrarConexion(cnx)

    def buscar(self,cadena):
        cnx = self.conectar()
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM articulos WHERE descripcion LIKE '%"+str(cadena)+"%'")
        arreglo = []
        for articulo in cursor:
            arreglo.append(articulo)
        self.CerrarConexion(cnx)
        return arreglo

    def consultar(self):
        cnx = self.conectar()
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM articulos")
        arreglo = []
        for articulos in cursor:
            arreglo.append(articulos)
        self.CerrarConexion(cnx)
        return arreglo

    def consultarArticuloporId(self,id_articulo):
        cnx = self.conectar()
        cursor = cnx.cursor()
        sql_qry="""SELECT descripcion FROM articulos WHERE id_articulo = %s"""
        cursor.execute(sql_qry,(id_articulo,))

        arreglo = cursor.fetchall()
        self.CerrarConexion(cnx)
        return arreglo

    def eliminar(self,id_articulo):
        cnx = self.conectar()
        cursor = cnx.cursor()
        cursor.execute("DELETE FROM articulos WHERE id_articulo="+str(id_articulo))
        cnx.commit()
        self.CerrarConexion(cnx)

    def ModificarStock(self,id_articulo,stock):
        
        cnx = self.conectar()
        cursor = cnx.cursor()
        sql_qry="""UPDATE articulos SET stock = %s WHERE id_articulo = %s"""
        value_qry="""SELECT stock FROM articulos WHERE id_articulo = %s"""
        cursor.execute(value_qry,(id_articulo,))
        record=cursor.fetchone()
        stock_actual=float(record[0])
        if(stock_actual>=stock):
            cursor.execute(sql_qry,(stock_actual-stock,id_articulo))
            cnx.commit()    
            self.CerrarConexion(cnx)
            return True
        else:
            self.CerrarConexion(cnx)
            return False
        

class Clientes (Conexion):
    
    def insertar(self,di,rs,d,tel,ce,):
        cnx=self.conectar()
        cursor = cnx.cursor()
        cursor.execute("INSERT INTO clientes VALUES(null,'"+di+"','"+rs+"','"+d+"','"+tel+"','"+ce+"')")
        cnx.commit()
        self.CerrarConexion(cnx)

    def cargar(self,id_cliente):
        cnx=self.conectar()
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM cliente WHERE idp_cliente="+str(id_cliente))
        arreglo = []
        for cliente in cursor:
            arreglo.append(cliente)
        self.CerrarConexion(cnx)
        return arreglo

    def modificar(self,di,rs,d,tel,ce,id_cliente):
        cnx = self.conectar()
        cursor = cnx.cursor()
        cursor.execute("UPDATE profesor SET dni_cuit='"+di+"',razon_social='"+rs+"',domicilio='"+d+"',telefono='"+tel+"',celular='"+ce+"' WHERE id_cliente='"+str(id_cliente)+"'")
        cnx.commit()
        self.CerrarConexion(cnx)

    def buscar(self,cadena):
        cnx = self.conectar()
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM clientes WHERE razon_social LIKE '%"+str(cadena)+"%'")
        arreglo = []
        for cliente in cursor:
            arreglo.append(cliente)
        self.CerrarConexion(cnx)
        return arreglo

    def consultar(self):
        cnx = self.conectar()
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM clientes")
        arreglo = []
        for cliente in cursor:
            arreglo.append(cliente)
        self.CerrarConexion(cnx)
        return arreglo

    def eliminar(self,id_cliente):
        cnx = self.conectar()
        cursor = cnx.cursor()
        cursor.execute("DELETE FROM clientes WHERE id_cliente="+str(id_cliente))
        cnx.commit()
        self.CerrarConexion(cnx)
        
        
#Ventas
class Ventas(Conexion):

    def venta(self,id_articulo,data):
        cnx = self.conectar()
        cursor = cnx.cursor()
        sql_qry="SELECT FROM app_workana.articulos WHERE id_articulo =%s"
        iid=(id_articulo,)
        cursor.execute(sql_qry,iid)
        cnx.commit()
        sql_qry="INSERT INTO app_workana.ventas VALUES (null,%s,%s,%s,%s,%s)"
        cursor.execute(sql_qry,data)
        self.CerrarConexion(cnx)
        
#Metodo para vender

    def vender(self,id_articulo,id_cliente):
        cnx = self.conectar()
        cursor = cnx.cursor()
        cursor.execute("Select")
    
    def NuevaVenta(self,id_articulo,data):
        cnx = self.conectar()
        cursor = cnx.cursor()
        sql_qry="""INSERT INTO app_workana.ventas (id_cliente,id_usuario,
        fecha,hora,total,estado) VALUES (%s,%s,%s,%s,%s,%s)"""
        cursor.execute(sql_qry,data)
        cnx.commit()
        self.CerrarConexion(cnx)

    def consultarVentas(self):
        cnx = self.conectar()
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM ventas")
        arreglo = []
        for ventas in cursor:
            arreglo.append(ventas)
        self.CerrarConexion(cnx)
        return arreglo

    def EliminarVenta(self,id_venta):
        cnx = self.conectar()
        cursor = cnx.cursor()
        #print(id_venta)
        sql_qry="""DELETE FROM app_workana.det_venta WHERE id_venta = %s"""
        cursor.execute(sql_qry,(id_venta,))
        sql_qry="""DELETE FROM app_workana.ventas WHERE id_venta = %s"""
        cursor.execute(sql_qry,(id_venta,))
        #print("id eliminado")
        cnx.commit()
        self.CerrarConexion(cnx)

    def DetalleVenta(self,id_articulo,data):
        cnx = self.conectar()
        cursor = cnx.cursor()
        sql_qry="""INSERT INTO app_workana.det_venta (id_venta,id_articulo,
        cantidad,precio_venta,sub_total,estado) VALUES (%s,%s,%s,%s,%s,%s)"""
        cursor.execute(sql_qry,data)
        cnx.commit()
        self.CerrarConexion(cnx)

    def consultarUltimoIDventas(self):
        cnx = self.conectar()
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM ventas")
        arreglo = []
        for ventas in cursor:
            arreglo.append(ventas)
        self.CerrarConexion(cnx)
        return (arreglo[len(arreglo)-1][0])

    def consultarVentasporClientes(self,id_cliente):
        cnx = self.conectar()
        cursor = cnx.cursor()
        sql_qry="""SELECT * FROM ventas WHERE id_cliente = %s"""
        cursor.execute(sql_qry,(id_cliente,))

        arreglo = cursor.fetchall()
        self.CerrarConexion(cnx)
        return arreglo

    def consultarVentasporID(self,id_venta):
        cnx = self.conectar()
        cursor = cnx.cursor()
        sql_qry="""SELECT * FROM det_venta WHERE id_venta = %s"""
        cursor.execute(sql_qry,(id_venta,))

        arreglo = cursor.fetchall()
        self.CerrarConexion(cnx)
        return arreglo


