#import psycopg2
#from psycopg2.extras import RealDictCursor
from tkinter import ttk
from tkinter import *

#conn = psycopg2.connect("host=localhost dbname=videotk user=postgres password=1234")
#conn.set_client_encoding('UTF8')

class Empleado():

    def __init__(self, window):
        self.wind = window
        self.wind.title('NOMINA EMPLEADOS')

        # Creating a Frame Container

        frame = LabelFrame(self.wind, text='Registre el nuevo Empleado')
        frame.grid(row=0, column=0, columnspan=3, pady=20)

        # Name Input
        Label(frame, text='Nombre: ').grid(row=1, column= 0, columnspan=1)
        self.name = Entry(frame)
        self.name.focus()

        self.name.grid(row=1, column=1)

        # Price Input

        Label(frame, text='Salario: ').grid(row=2, column=0)
        self.price = Entry(frame)
        self.price.grid(row=2, column=1)

        # Button Add Product
        ttk.Button(frame, text='Guardar Empleado').grid(row=3, columnspan=2, sticky=W + E)

        # Table


        self.tree = ttk.Treeview( height=10, columns=3)
        self.tree.grid(row=4, column=0, columnspan=2)
        self.tree.heading('#0', text='Nombre', anchor=CENTER)
        self.tree.heading('#1', text='Salario', anchor=CENTER)

        self.get_empleados()

    def get_empleados (self):


        #cur = conn.cursor(cursor_factory=RealDictCursor)
        #cur.execute("""select * from empleado """)

        #rows = [cur.fetchall()]

        rows=["pepe","jose","juan"]
        for row in rows:
            self.tree.insert('', 0,  text=row[1:], values=row[2:])



if __name__ == '__main__':
    window = Tk()
    application = Empleado(window)
    window.mainloop()