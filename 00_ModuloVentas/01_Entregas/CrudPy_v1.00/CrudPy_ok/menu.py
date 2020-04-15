from tkinter import *
from tkinter import ttk
from tkinter.ttk import Style
from tkinter import messagebox
from clasess import *
import tkinter as tk
import time
from tkinter import filedialog
import csv

############################################################


def cargarA():
	a = Articulos()
	arreglo = a.cargar(arregloIDA1[comboA1.current()])
	for c in arreglo:
		descripcionA1.set(c[1])
		codigoA1.set(c[2])
		StockA1.set(c[3])
		precio_vtaA1.set(c[4])

def insertar():
	a = Articulos()
	a.insertar(descripcion.get(), codigo.get(), stock.get(),precio_vta.get())
	descripcion.set("")
	codigo.set("")
	stock.set("")
	precio_vta.set("")
	messagebox.showinfo("Mensaje", "Articulo Insertado")

def modificarA():
	AM=messagebox.askquestion("ADVERTENCIA","DESEA MODIFICAR...??")
	if AM=="yes":
		a = Articulos()
		a.modificar(descripcionA1.get(),codigoA1.get(),stockA1.get(),precio_vtaA1.get(),arregloIdA1[comboA1.current()])
		nombreA1.set("")
		apellidoA1.set("")
		dniA1.set("")
		direccionA1.set("")
		messagebox.showinfo("Mensaje", "articulo Modificado")
	else:
		messagebox.showinfo("Mensaje", "articulo NO Modificado")

def consultarA():
	t.config(state=NORMAL)
	t.delete("1.0",END)
	t.insert(INSERT, "descripcion\t\tcodigo\t\tstock\t\tprecio_vta\t\n")
	a = Articulos()
	arreglo = a.consultar()
	for c in arreglo:
		t.insert(INSERT,c[1]+"\t\t"+c[2]+"\t\t"+str(c[3])+"\t\t"+str(c[4])+"\n")
		t.place(x=20,y=100)
		t.config(state=DISABLED)

def buscarA(Key):
	if(cajaC.get()==""):
		consultarA()
	else:
		t.config(state=NORMAL)
		t.delete("1.0",END)
		t.insert(INSERT, "descripcion\t\tcodigo\t\tstock\t\tprecio_vta\t\n")
		a = Articulos()
		arreglo = a.buscar(cajaC.get())
		for c in arreglo:
			t.insert(INSERT,c[1]+"\t\t"+c[2]+"\t\t"+c[3]+"\t\t"+c[4]+"\n")
			t.place(x=20,y=100)
			t.config(state=DISABLED)

def eliminarA():
	AE=messagebox.askquestion("ADVERTENCIA","DESEA ELIMINAR...??")
	if AE=="yes":
		print(comboA.current())
		a = Articulos()
		a.eliminar(arregloIdA[comboA.current()])
		messagebox.showinfo("Mensaje", "Articulo Eliminado")
		llenarComboEA()
	else:
		messagebox.showinfo("Mensaje", "Articulo no se elimino")


def llenarComboEA():
	a = Articulos()
	arreglo = a.consultar()
	arregloArticulo = []
	global arregloIdA
	arregloIdA = []
	for c in arreglo:
		arregloArticulo.append(c[1]+" "+c[2])
		arregloIdA.append(c[0])
		comboA['values']=arregloArticulo
		comboA.current()

def llenarComboMA():
	a = Articulos()
	arreglo = a.consultar()
	arregloArticulo = []
	global arregloIdA1
	arregloIdA1 = []
	for c in arreglo:
		arregloArticulo.append(c[1]+" "+c[2])
		arregloIdA1.append(c[0])
		comboA1['values']=arregloArticulo
		comboA1.current()

def volverIA():
	windows4.destroy()
	ventana_principal()

def volverMA():
	windows5.destroy()
	ventana_principal()

def volverCA():
	windows6.destroy()
	ventana_principal()

def volverEA():
	windows7.destroy()
	ventana_principal()

def articulo_ingresar():
	ventana.destroy()
	global windows4
	windows4=Tk()
	windows4.title("INGRESAR Articulo")
	windows4.geometry("550x550+450+100")
	windows4.configure(bg="white")
	global descripcion
	global codigo
	global stock
	global precio_vta
	descripcion = StringVar()
	codigo = StringVar()
	stock = StringVar()
	precio_vta =StringVar()
	Label(windows4,text="INGRESAR Articulos ",fg="DarkGrey",bg="white",font=("Times New Roman",20)).place(x=190,y=10)
	Label(windows4,text="Descripcion : ",fg="black",bg="white",font=("Times New Roman",10)).place(x=150,y=90)
	Label(windows4,text="Codigo : ",fg="black",bg="white",font=("Times New Roman",10)).place(x=150,y=140)
	Label(windows4,text="Stock : ",fg="black",bg="white",font=("Times New Roman",10)).place(x=150,y=190)
	Label(windows4,text="Precio de Venta : ",fg="black",bg="white",font=("Times New Roman",10)).place(x=150,y=240)
	#####
	Entry(windows4,textvariable=descripcion).place(x=250,y=90)
	Entry(windows4,textvariable=codigo).place(x=250,y=140)
	Entry(windows4,textvariable=stock).place(x=250,y=190)
	Entry(windows4,textvariable=precio_vta).place(x=250,y=240)
	#####
	Button(windows4,text="GUARDAR",bg="white",fg="black",command=insertar,font=("Times New Roman",10)).place(x=250,y=300,width=100, height=30)
	Button(windows4,text="SALIR",bg="white",fg="red",command=windows4.destroy,font=("Times New Roman",10)).place(x=490,y=300,width=100, height=30)
	Button(windows4,text="VOLVER",bg="white",fg="black",command=volverIA,font=("Times New Roman",10)).place(x=370,y=300,width=100, height=30)
	mainloop()

def articulo_modificar():
	ventana.destroy()
	global windows5
	windows5=Tk()
	windows5.title("MODIFICAR Producto")
	windows5.geometry("550x550+350+100")
	windows5.configure(bg="white")
	global descripcionA1 
	global codigoA1 
	global stockA1 
	global precio_vtaA1 
	descripcionA1 = StringVar()
	codigoA1 = StringVar()
	stockA1 = StringVar()
	precio_vtaA1 = StringVar()
	Label(windows5,text="SELECCIONAR : ",fg="black",bg="white").place(x=150,y=90)
	global comboA1
	comboA1 = ttk.Combobox(windows5)
	comboA1.place(x=240,y=90)
	llenarComboMA()
	Label(windows5,text="MODIFICAR Producto ",fg="Darkgrey",bg="white",font=("Times New Roman",20)).place(x=190,y=10)
	Button(windows5,text="CARGAR",bg="white",fg="black",command=cargarA,font=("Times New Roman",10)).place(x=420,y=80,width=100, height=30)
	Label(windows5,text="NOMBRE : ",fg="black",bg="white",font=("Times New Roman",10)).place(x=150,y=150)
	Label(windows5,text="APELLIDO : ",fg="black",bg="white",font=("Times New Roman",10)).place(x=150,y=190)
	Label(windows5,text="DNI : ",fg="black",bg="white",font=("Times New Roman",10)).place(x=150,y=230)
	Label(windows5,text="DIRECCION : ",fg="black",bg="white",font=("Times New Roman",10)).place(x=150,y=270)
	############
	Entry(windows5,textvariable=descripcionA1).place(x=250,y=150)
	Entry(windows5,textvariable=codigoA1).place(x=250,y=190)
	Entry(windows5,textvariable=stockA1).place(x=250,y=230)
	Entry(windows5,textvariable=precio_vtaA1).place(x=250,y=270)
	Button(windows5,text="MODIFICAR",bg="white",fg="black",command=modificarA,font=("Times New Roman",10)).place(x=250,y=350,width=100, height=30)
	Button(windows5,text="SALIR",bg="white",fg="red",command=windows5.destroy,font=("Times New Roman",10)).place(x=490,y=350,width=100, height=30)
	Button(windows5,text="VOLVER",bg="white",fg="black",command=volverMA,font=("Times New Roman",10)).place(x=370,y=350,width=100, height=30)
	mainloop()

def articulo_consultar():
	ventana.destroy()
	global cajaC
	global t
	global windows6
	windows6=Tk()
	windows6.title("CONSULTAR Producto")
	windows6.geometry("550x350+350+100")
	windows6.configure(bg="white")
	cajaC = StringVar()
	t = Text(windows6,width=76,height=23)
	consultarA()
	Label(windows6,text="CONSULTAR Producto ",fg="blue",bg="white",font=("Times New Roman",20)).place(x=190,y=10)
	Label(windows6,text="BUSCAR: ",fg="black",bg="white",font=("Times New Roman",10)).place(x=20,y=70)
	entry = Entry(windows6,textvariable=cajaC)
	entry.place(x=80,y=70)
	entry.bind("<KeyRelease>",buscarA)
	Button(windows6,text="SALIR",bg="white",fg="red",command=windows6.destroy,font=("Times New Roman",10)).place(x=520,y=60,width=100, height=30)
	Button(windows6,text="VOLVER",bg="white",fg="black",command=volverCA,font=("Times New Roman",10)).place(x=400,y=60,width=100, height=30)
	mainloop()

def articulo_eliminar():
	ventana.destroy()
	global windows7
	windows7=Tk()
	windows7.title("ELIMINAR Producto")
	windows7.geometry("650x450+350+100")
	windows7.configure(bg="white")
	Label(windows7,text="SELECCIONAR : ",fg="black",bg="white",font=("Times New Roman",10)).place(x=160,y=100)
	global comboA
	comboA = ttk.Combobox(windows7)
	comboA.place(x=240,y=100)
	llenarComboEA()
	Label(windows7,text="ELIMINAR Producto ",fg="blue",bg="white",font=("Times New Roman",20)).place(x=190,y=10)
	Button(windows7,text="ELIMINAR",bg="white",fg="black",command=eliminarA,font=("Times New Roman",10)).place(x=420,y=90,width=100, height=30)
	Button(windows7,text="SALIR",bg="white",fg="red",command=windows7.destroy,font=("Times New Roman",10)).place(x=370,y=200,width=100, height=30)
	Button(windows7,text="VOLVER",bg="white",fg="black",command=volverEA,font=("Times New Roman",10)).place(x=250,y=200,width=100, height=30)
	mainloop()


############################################################

def cargarC():
	C = clientes()
	arreglo = c.cargar(arregloIdC1[comboC1.current()])
	for c in arreglo:
		dni_cuitC1.set(c[1])
		razon_socialC1.set(c[2])
		domicilioC1.set(c[3])
		telefonoC1.set(c[4])
		celularC1.set(c[5]) 

def insertarC():
	c= Clientes()
	c.insertar(dni_cuitC.get(),razon_socialC.get(),domicilioC.get(),telefonoC.get(),celularC.get())
	dni_cuitC.set("")
	razon_socialC.set("")
	domicilioC.set("")
	telefonoC.set("")
	celularC.set("")
	messagebox.showinfo("Mensaje", "Cliente Insertado")

def modificarC():
	CM=messagebox.askquestion("ADVERNTENCIA","DESEA MODIFICAR...??")
	if CM=="yes":
		c = Clientes()
		c.modificar(dni_cuitC1.get(),razon_socialC1.get(),domicilioC1.get(),telefonoC1.get(),celularC1.get(),arregloIdC1[comboC1.current()])
		dni_cuitC.set("")
		razon_socialC.set("")
		domicilioC.set("")
		telefonoC.set("")
		celularC.set("")
		messagebox.showinfo("Mensaje", "Cliente Modificado")
	else:
		messagebox.showinfo("Mensaje","Cliente No Modificado")

def consultarP():
	r.config(state=NORMAL)
	r.delete("1.0",END)
	r.insert(INSERT, "Nombre\t\tApellido\t\tDNI\t\tDireccion\t\tTelefono\t\n")
	p = Clientes()
	arreglo = p.consultar()
	for c in arreglo:
		r.insert(INSERT,c[1]+"\t\t"+c[2]+"\t\t"+c[3]+"\t\t"+c[4]+"\t\t"+c[5]+"\n")
		r.place(x=20,y=100)
		r.config(state=DISABLED)

def buscarP(Key):
	if(cajaB.get()==""):
		consultarP()
	else:
		r.config(state=NORMAL)
		r.delete("1.0",END)
		r.insert(INSERT, "Nombre\t\tApellido\t\tDNI\t\tDireccion\t\tTelefono\t\n")
		p = Clientes()
		arreglo = p.buscar(cajaB.get())
	for c in arreglo:
		r.insert(INSERT,c[1]+"\t\t"+c[2]+"\t\t"+c[3]+"\t\t"+c[4]+"\t\t"+c[5]+"\n")
		r.place(x=20,y=100)
		r.config(state=DISABLED)

def eliminarP():
	PE=messagebox.askquestion("ADVERTENCIA","DESEA ELIMNAR...??")
	if PE=="yes":
		print(comboC.current())
		p = Clientes()
		p.eliminar(arregloIdP[comboC.current()])
		messagebox.showinfo("Mensaje", "Cliente Eliminado")
		llenarComboEP()
	else:
		messagebox.showinfo("Mensaje","Cliente NO Eliminado")

def llenarComboEP():
	p = Clientes()
	arreglo = p.consultar()
	arregloCliente = []
	global arregloIdC
	arregloIdP = []
	for c in arreglo:
		arregloCliente.append(c[1]+" "+c[2])
		arregloIdP.append(c[0])
		comboC['values']=arregloCliente
		comboC.current()

def llenarComboMC():
	C = Clientes()
	arreglo = C.consultar()
	arregloCliente = []
	global arregloIdP1
	arregloIdP1 = []
	for c in arreglo:
		arregloCliente.append(c[1]+" "+c[2])
		arregloIdP1.append(c[0])
		comboC1['values']=arregloCliente
		comboC1.current()

def volverIP():
	windows.destroy()
	ventana_principal()

def volverMC():
	windows1.destroy()
	ventana_principal()

def volverCC():
	windows2.destroy()
	ventana_principal()

def volverEC():
	windows3.destroy()
	ventana_principal()

def Cliente_ingresar():
	ventana.destroy()
	global windows
	windows=Tk()
	windows.title("INGRESAR Cliente")
	windows.geometry("650x550+450+100")
	windows.configure(bg="white")
	global nombreP
	global apellidoP
	global dniP
	global direccionP
	global telefonoP
	nombreP = StringVar()
	apellidoP = StringVar()
	dniP = StringVar()
	direccionP =StringVar()
	telefonoP = StringVar()
	Label(windows,text="INGRESAR Cliente ",fg="blue",bg="white",font=("Times New Roman",20)).place(x=190,y=10)
	Label(windows,text="NOMBRE : ",fg="black",bg="white",font=("Times New Roman",10)).place(x=150,y=90)
	Label(windows,text="APELLIDO : ",fg="black",bg="white",font=("Times New Roman",10)).place(x=150,y=140)
	Label(windows,text="DNI : ",fg="black",bg="white",font=("Times New Roman",10)).place(x=150,y=190)
	Label(windows,text="DIRECCION : ",fg="black",bg="white",font=("Times New Roman",10)).place(x=150,y=240)
	Label(windows,text="TELEFONO :",fg="black",bg="white",font=("Times New Roman",10)).place(x=150,y=290)
	Entry(windows,textvariable=nombreP).place(x=250,y=90)
	Entry(windows,textvariable=apellidoP).place(x=250,y=140)
	Entry(windows,textvariable=dniP).place(x=250,y=190)
	Entry(windows,textvariable=direccionP).place(x=250,y=240)
	Entry(windows,textvariable=telefonoP).place(x=250,y=290)
	Button(windows,text="GUARDAR",bg="white",fg="black",command=insertarP,font=("Times New Roman",10)).place(x=250,y=350,width=100, height=30)
	Button(windows,text="SALIR",bg="white",fg="red",command=windows.destroy,font=("Times New Roman",10)).place(x=490,y=350,width=100, height=30)
	Button(windows,text="VOLVER",bg="white",fg="black",command=volverIP,font=("Times New Roman",10)).place(x=370,y=350,width=100, height=30)
	mainloop()

def Cliente_modificar():
	ventana.destroy()
	global windows1
	windows1=Tk()
	windows1.title("MODIFICAR Cliente")
	windows1.geometry("650x450+350+100")
	windows1.configure(bg="white")
	global nombreP1 
	global apellidoP1
	global dniP1 
	global direccionP1 
	global telefonoP1
	nombreP1 = StringVar()
	apellidoP1 = StringVar()
	dniP1 = StringVar()
	direccionP1 = StringVar()
	telefonoP1 = StringVar()
	Label(windows1,text="SELECCIONAR : ",fg="black",bg="white",font=("Times New Roman",10)).place(x=150,y=90)
	global comboP1
	comboP1 = ttk.Combobox(windows1)
	comboP1.place(x=240,y=90)
	llenarComboMC()
	Label(windows1,text="MODIFICAR Cliente ",fg="blue",bg="white",font=("Times New Roman",20)).place(x=190,y=10)
	Button(windows1,text="CARGAR",bg="white",fg="black",command=cargarP,font=("Times New Roman",10)).place(x=420,y=80,width=100, height=30)
	Label(windows1,text="NOMBRE : ",fg="black",bg="white",font=("Times New Roman",10)).place(x=150,y=140)
	Label(windows1,text="APELLIDO : ",fg="black",bg="white",font=("Times New Roman",10)).place(x=150,y=170)
	Label(windows1,text="DNI : ",fg="black",bg="white",font=("Times New Roman",10)).place(x=150,y=200)
	Label(windows1,text="DIRECCION : ",fg="black",bg="white",font=("Times New Roman",10)).place(x=150,y=240)
	Label(windows1,text="TELEFONO : ",fg="black",bg="white",font=("Times New Roman",10)).place(x=150,y=270)
	Entry(windows1,textvariable=nombreP1).place(x=250,y=140)
	Entry(windows1,textvariable=apellidoP1).place(x=250,y=170)
	Entry(windows1,textvariable=dniP1).place(x=250,y=200)
	Entry(windows1,textvariable=direccionP1).place(x=250,y=240)
	Entry(windows1,textvariable=telefonoP1).place(x=250,y=270)
	Button(windows1,text="MODIFICAR",bg="white",fg="black",command=modificarP,font=("Times New Roman",10)).place(x=250,y=350,width=100, height=30)
	Button(windows1,text="SALIR",bg="white",fg="red",command=windows1.destroy,font=("Times New Roman",10)).place(x=490,y=350,width=100, height=30)
	Button(windows1,text="VOLVER",bg="white",fg="black",command=volverMP,font=("Times New Roman",10)).place(x=370,y=350,width=100, height=30)
	mainloop()

def Cliente_consultar():
	ventana.destroy()
	global cajaB
	global r
	global windows2
	windows2=Tk()
	windows2.title("CONSULTAR Cliente")
	windows2.geometry("650x450+350+100")
	windows2.configure(bg="white")
	cajaB = StringVar()
	r = Text(windows2,width=76,height=23)
	consultarP()
	Label(windows2,text="BUSCAR: ",fg="black",bg="white",font=("Times New Roman",10)).place(x=20,y=70)
	entry = Entry(windows2,textvariable=cajaB)
	entry.place(x=80,y=70)
	entry.bind("<KeyRelease>",buscarP)
	Label(windows2,text="CONSUNTAR Cliente ",fg="blue",bg="white",font=("Times New Roman",20)).place(x=190,y=10)
	Button(windows2,text="SALIR",bg="white",fg="red",command=windows2.destroy,font=("Times New Roman",10)).place(x=520,y=60,width=100, height=30)
	Button(windows2,text="VOLVER",bg="white",fg="black",command=volverCP,font=("Times New Roman",10)).place(x=400,y=60,width=100, height=30)
	mainloop()

def Cliente_eliminar():
	ventana.destroy()
	global windows3
	windows3=Tk()
	windows3.title("ELIMINAR Cliente")
	windows3.geometry("650x450+350+100")
	windows3.configure(bg="white")
	Label(windows3,text="SELECCIONAR : ",fg="black",bg="white",font=("Times New Roman",10)).place(x=160,y=100)
	global comboP
	comboP = ttk.Combobox(windows3)
	comboP.place(x=240,y=100)
	llenarComboEP()
	Label(windows3,text="ELIMINAR Cliente ",fg="blue",bg="white",font=("Times New Roman",20)).place(x=190,y=10)
	Button(windows3,text="ELIMINAR",bg="white",fg="black",command=eliminarP,font=("Times New Roman",10)).place(x=420,y=90,width=100, height=30)
	Button(windows3,text="SALIR",bg="white",fg="red",command=windows3.destroy,font=("Times New Roman",10)).place(x=370,y=200,width=100, height=30)
	Button(windows3,text="VOLVER",bg="white",fg="black",command=volverEP,font=("Times New Roman",10)).place(x=250,y=200,width=100, height=30)
	mainloop()

##############################################################################################
#-------------------------------MODULO VENTAS----------------------------------

class ModuloVentas:
	def __init__(self):

		self.windowsVender=tk.Tk()
		self.windowsVender.title("Venta de Productos")

		self.articulosTotal=Articulos()
		self.ventasTotal=Ventas()

		self.miFrame_1 = Frame(self.windowsVender)
		self.miFrame_1.pack()

		self.tituloLabel=Label(self.miFrame_1,text="Articulos",fg="blue",bg="white",font=("Times New Roman",20))
		self.tituloLabel.grid(row=0, column=0,padx=10,pady=10,sticky="we",columnspan=6)

		self.botonVender = Button(self.miFrame_1, text="VENDER",width=15,command=self.realizarVenta)
		self.botonVender.grid(row=1, column=4,padx=10,pady=10,sticky="we")

		self.datacuadroCliente = StringVar()
		self.datacuadroUsuario = StringVar()
		self.datacuadroCantidad =IntVar()
		self.datacuadroEstado = StringVar()

		self.cuadroCliente = Entry(self.miFrame_1, textvariable=self.datacuadroCliente)
		self.cuadroCliente.grid(row=1, column=1, padx=10, pady=10)
		self.cuadroCliente.config(justify="center")

		self.cuadroUsuario = Entry(self.miFrame_1, textvariable=self.datacuadroUsuario)
		self.cuadroUsuario.grid(row=2, column=1, padx=10, pady=10)
		self.cuadroUsuario.config(justify="center")

		self.cuadroCantidad = Entry(self.miFrame_1, textvariable=self.datacuadroCantidad)
		self.cuadroCantidad.grid(row=1, column=3, padx=10, pady=10,)
		self.cuadroCantidad.config(justify="center")

		self.cuadroEstado = Entry(self.miFrame_1, textvariable=self.datacuadroEstado)
		self.cuadroEstado.grid(row=2, column=3, padx=10, pady=10,)
		self.cuadroEstado.config(justify="center")

		self.cuadroClienteLabel = Label(self.miFrame_1, text="Cliente: ")
		self.cuadroClienteLabel.grid(row=1, column=0, padx=10, pady=10)

		self.cuadroUsuarioLabel = Label(self.miFrame_1, text="Usuario: ")
		self.cuadroUsuarioLabel.grid(row=2, column=0, padx=10, pady=10)

		self.cuadroCantidadLabel = Label(self.miFrame_1, text="Cantidad: ")
		self.cuadroCantidadLabel.grid(row=1, column=2, padx=10, pady=10)

		self.cuadroEstadoLabel = Label(self.miFrame_1, text="Estado: ")
		self.cuadroEstadoLabel.grid(row=2, column=2, padx=10, pady=10)

		self.miFrame_2 = Frame(self.windowsVender)
		self.miFrame_2.pack()

		self.tree = ttk.Treeview(self.miFrame_2,columns = ("id_articulo","descripcion","codigo","stock","precio_vta"))   
		self.tree.grid(row=1,column=1,padx=10,pady=10)

		self.tree['show']='headings'
		self.tree.heading('#0', text='column0', anchor=tk.W)
		self.tree.heading('#1', text='id_articulo', anchor=tk.W)
		self.tree.heading('#2', text='descripcion', anchor=tk.W)
		self.tree.heading('#3', text='codigo', anchor=tk.W)
		self.tree.heading('#4', text='stock', anchor=tk.W)
		self.tree.heading('#5', text='precio_vta', anchor=tk.W)

		self.tree.column('#0',width=100,minwidth=70,stretch=tk.YES)
		self.tree.column('#1',width=100,minwidth=70,stretch=tk.YES)
		self.tree.column('#2',width=100,minwidth=70,stretch=tk.YES)
		self.tree.column('#3',width=100,minwidth=70,stretch=tk.YES)
		self.tree.column('#4',width=100,minwidth=70,stretch=tk.YES)
		self.tree.column('#5',width=100,minwidth=70,stretch=tk.YES)

		for row in self.articulosTotal.consultar():
			self.tree.insert('',END, values=row) 

		self.scrollVert=Scrollbar(self.miFrame_2,command=self.tree.yview)
		self.scrollVert.grid(row=1,column=4,sticky="nsnew")
		self.tree.config(yscrollcommand=self.scrollVert.set)

		self.windowsVender.mainloop()


	def InsertarArticulos(self,data):
		for row in data:
			self.tree.insert('',END, values=row) 

	def realizarVenta(self):
		try:	
			listadata=self.leerInfoInputBox()
			item = self.tree.focus()
			idArticulo=self.tree.item(item,"values")[0]
			valorVenta=float(self.tree.item(item,"values")[4])
			miTupla=(listadata[0],listadata[1],time.strftime("%y/%m/%d"),time.strftime("%H:%M:%S"),valorVenta*listadata[2],listadata[3])
			#print(time.strftime("%y/%m/%d"))
			miVentaNueva=Ventas()
			miVentaNueva.NuevaVenta(idArticulo,miTupla)
			articulosTotal=Articulos()
			#hayStock(idArticulo)
			if(articulosTotal.ModificarStock(idArticulo,listadata[2])==True):
				miDetalle=(idArticulo,listadata[2],valorVenta,valorVenta*listadata[2],listadata[3])
				self.UpdateTreeViewArticulos()	
				miIDventas=((self.ventasTotal.consultarUltimoIDventas(),))
				miVentaNueva.DetalleVenta(idArticulo,miIDventas+miDetalle)
				messagebox.showinfo("Ventas", "venta exitosa!")
			else:
				messagebox.showwarning("Ventas", "No hay stock!")

		except:
			messagebox.showinfo("Ventas", "Debe completar todos los campos y selecionar el Articulo a Vender")

	def UpdateTreeViewArticulos(self):
		for row in self.tree.get_children():
			self.tree.delete(row)
		for row in self.articulosTotal.consultar():
			self.tree.insert('',END, values=row) 
	
	def leerInfoInputBox(self):
		try:
			listadata = [int(self.cuadroCliente.get()), int(self.cuadroUsuario.get()),float(self.cuadroCantidad.get()),self.cuadroEstado.get()]
			return listadata
		except:
			messagebox.showwarning("Ventas", "Error en los datos")

#-----------------------------------------------MODULO VENTAS GENERALES-----------------------------------------------

class ModuloVentasGenerales:

	def __init__(self):

		self.windowsVender=tk.Tk()
		self.windowsVender.title("Venta Generales")

		self.articulosTotal=Articulos()

		self.miFrame_1 = Frame(self.windowsVender)
		self.miFrame_1.pack()

		self.botonCancelar = Button(self.miFrame_1, text="CANCELAR VENTA",width=15,command=self.ModificarVenta)
		self.botonCancelar.grid(row=2, column=4,padx=10,pady=10,sticky="we")
		
		self.miFrame_3 = Frame(self.windowsVender)
		self.miFrame_3.pack()
		self.ventasTotal=Ventas()

		self.tituloLabel=Label(self.miFrame_3,text="Ventas",fg="blue",bg="white",font=("Times New Roman",20))
		self.tituloLabel.grid(row=0, column=1, padx=10, pady=10,sticky="we")

		self.treeVentas = ttk.Treeview(self.miFrame_3,columns = ("id_venta","id_cliente","id_usuario","fecha","hora","total","estado"))   
		self.treeVentas.grid(row=1,column=1,padx=10,pady=10)
		self.treeVentas['show']='headings'
		self.treeVentas.heading('#0', text='column0', anchor=tk.W)
		self.treeVentas.heading('#1', text='id_venta', anchor=tk.W)
		self.treeVentas.heading('#2', text='id_cliente', anchor=tk.W)
		self.treeVentas.heading('#3', text='id_ususario', anchor=tk.W)
		self.treeVentas.heading('#4', text='fecha', anchor=tk.W)
		self.treeVentas.heading('#5', text='hora', anchor=tk.W)
		self.treeVentas.heading('#6', text='total', anchor=tk.W)
		self.treeVentas.heading('#7', text='estado', anchor=tk.W)

		self.treeVentas.column('#0',width=70,minwidth=70,stretch=tk.YES)
		self.treeVentas.column('#1',width=70,minwidth=70,stretch=tk.YES)
		self.treeVentas.column('#2',width=70,minwidth=70,stretch=tk.YES)
		self.treeVentas.column('#3',width=70,minwidth=70,stretch=tk.YES)
		self.treeVentas.column('#4',width=70,minwidth=70,stretch=tk.YES)
		self.treeVentas.column('#5',width=70,minwidth=70,stretch=tk.YES)
		self.treeVentas.column('#6',width=70,minwidth=70,stretch=tk.YES)
		self.treeVentas.column('#7',width=70,minwidth=70,stretch=tk.YES)

		for row in self.ventasTotal.consultarVentas():
			self.treeVentas.insert('',END, values=row)

		self.scrollVert2=Scrollbar(self.miFrame_3,command=self.treeVentas.yview)
		self.scrollVert2.grid(row=1,column=2,sticky="nsnew")
		self.treeVentas.config(yscrollcommand=self.scrollVert2.set)

		self.windowsVender.mainloop()

	def UpdateTreeViewVentas(self):
		for row in self.treeVentas.get_children():
			self.treeVentas.delete(row)
		for row in self.ventasTotal.consultarVentas():
			self.treeVentas.insert('',END, values=row)

	def ModificarVenta(self):
		try:
			miVenta=Ventas()
			itemVenta = self.treeVentas.focus()
			#print(itemVenta)
			idVentas=int(self.treeVentas.item(itemVenta,"values")[0])
			opcion=messagebox.askquestion("Eliminar","Desea eliminar la venta Selecionada?")
			miVenta.EliminarVenta(idVentas)
			self.UpdateTreeViewVentas()
		except:
			messagebox.showwarning("ModificarVenta","No ha selecionado ninguna venta")

#-----------------------------------------------MODULO CONSULTAS POR CLIENTES-----------------------------------------------

class ModuloConsultasVentas:

	def __init__(self):
		self.windows=tk.Tk()
		self.windows.title("Consultar por Cliente")
		
		self.sumatoria=StringVar(self.windows,"0.0")
		
		self.miFrame_1 = Frame(self.windows)
		self.miFrame_1.pack()

		self.titulo=Label(self.miFrame_1,text="Consultar por Cliente",fg="blue",bg="white",font=("Times New Roman",20))
		self.titulo.grid(row=0, column=1,padx=10,pady=10,sticky="we",columnspan=6)
		
		self.datacuadroCliente2 = StringVar()
		
		self.cuadroCliente = Entry(self.miFrame_1, textvariable=self.datacuadroCliente2)
		self.cuadroCliente.grid(row=1, column=1, padx=10, pady=10)
		self.cuadroCliente.config(justify="center")

		self.cuadroClienteLabel = Label(self.miFrame_1, text="Cliente: ")
		self.cuadroClienteLabel.grid(row=1, column=0, padx=10, pady=10)

		self.botonSet = Button(self.miFrame_1, text="BUSCAR",width=15,command=self.buscarPorCliente)
		self.botonSet.grid(row=1, column=2,padx=10,pady=10,sticky="we")

		self.cuadroSumatoria = Label(self.miFrame_1, text="Sumatoria: ")
		self.cuadroSumatoria.grid(row=2, column=0, padx=10, pady=10)

		self.cuadroValueSumatoria = Label(self.miFrame_1, textvariable=self.sumatoria)
		self.cuadroValueSumatoria.grid(row=2, column=1, padx=10, pady=10)

		self.miFrame = Frame(self.windows)
		self.miFrame.pack()

		self.treeConsultas = ttk.Treeview(self.miFrame,columns = ("id_cliente","id_venta","descripcion","cantidad","precio_vta"))   
		self.treeConsultas.grid(row=1,column=1,padx=10,pady=10)

		self.treeConsultas['show']='headings'
		self.treeConsultas.heading('#0', text='column0', anchor=tk.W)
		self.treeConsultas.heading('#1', text='id_cliente', anchor=tk.W)
		self.treeConsultas.heading('#2', text='id_venta', anchor=tk.W)
		self.treeConsultas.heading('#3', text='descripcion', anchor=tk.W)
		self.treeConsultas.heading('#4', text='cantidad', anchor=tk.W)
		self.treeConsultas.heading('#5', text='precio_vta', anchor=tk.W)

		self.treeConsultas.column('#0',width=100,minwidth=70,stretch=tk.YES)
		self.treeConsultas.column('#1',width=100,minwidth=70,stretch=tk.YES)
		self.treeConsultas.column('#2',width=100,minwidth=70,stretch=tk.YES)
		self.treeConsultas.column('#3',width=100,minwidth=70,stretch=tk.YES)
		self.treeConsultas.column('#4',width=100,minwidth=70,stretch=tk.YES)
		self.treeConsultas.column('#5',width=100,minwidth=70,stretch=tk.YES)

		self.scrollVert=Scrollbar(self.miFrame,command=self.treeConsultas.yview)
		self.scrollVert.grid(row=1,column=4,sticky="nsnew")
		self.treeConsultas.config(yscrollcommand=self.scrollVert.set)
		
		self.windows.mainloop()

	def leerInfoInputCliente(self):
		try:
			data = int(self.cuadroCliente.get())
			return data
		except:
			messagebox.showwarning("Clientes", "Error en los datos")
	
	def DeleteTreeViewConsultas(self):
		for row in self.treeConsultas.get_children():
			self.treeConsultas.delete(row)		

	def buscarPorCliente(self):
		self.DeleteTreeViewConsultas()
		suma=0.0
		milista=[]
		miVentaConsulta=Ventas()
		Id_cliente=self.leerInfoInputCliente()
		listdata=miVentaConsulta.consultarVentasporClientes(Id_cliente)
		for i in listdata:
			id_ventas=i[0]
			tupladatos=(Id_cliente,id_ventas)
			listdataVentas=miVentaConsulta.consultarVentasporID(id_ventas)
			for a in listdataVentas:
				miArticulo=Articulos()
				descripcion=miArticulo.consultarArticuloporId(a[2])
				milista.append(tupladatos + (descripcion,a[3],a[4]))
				suma=suma+a[3]*a[4]
		for row in milista:
			self.treeConsultas.insert('',END, values=row)
		self.sumatoria.set(str(suma))

#-----------------------------------------------MODULO GEN REPORTES-----------------------------------------------

class ModuloReportes:

	def __init__(self,dataReportes):
		self.raiz = Tk()
		self.datosaCsv=dataReportes
		self.raiz.title("Gen Reporte")

		self.barraMenu = Menu(self.raiz)
		self.raiz.config(menu=self.barraMenu)
		self.datacuadroguardar=StringVar(self.raiz,"")
		
		self.Infomenu = Menu(self.barraMenu, tearoff=0)
		self.Infomenu.add_command(label="Salir", command=self.salirAplicacion)
		self.barraMenu.add_cascade(label="MENU", menu=self.Infomenu)
		
		self.miFrame = Frame(self.raiz, width=350, height=400)
		self.miFrame.pack()
	
		self.cuadroguardar = Entry(self.miFrame, textvariable=self.datacuadroguardar)
		self.cuadroguardar.grid(row=2, column=1, padx=10, pady=10, columnspan=1)
		self.cuadroguardar.config(justify="center")

		self.botonSave=Button(self.miFrame,text="...",command=self.saveFichero)
		self.botonSave.grid(row=2, column=2, padx=10, pady=10,columnspan=1)

		self.guardarLabel = Label(self.miFrame, text="Guardar: ")
		self.guardarLabel.grid(row=2, column=0, padx=10, pady=10,sticky="e")

		self.botonSet = Button(self.miFrame, text="Generar Reporte", width=15,command=lambda:self.genReporte(self.datosaCsv))
		self.botonSet.grid(row=3, column=1, padx=10, pady=10)

		self.raiz.mainloop()

	def borrarInputBox(self):
		self.datacuadroguardar.set("")

	def saveFichero(self):
		fichero=filedialog.asksaveasfilename(title="Abrir",initialdir="C:/",filetypes=(("CSV files","*.csv"),("Todos los ficheros","*.*")))
		self.datacuadroguardar.set(fichero)

	def writeCSV_new(self,myData,filename):	
		myFile = open(filename,'a',newline='')
		with myFile:
			writer = csv.writer(myFile)
			writer.writerow(myData)
	
	def salirAplicacion(self):	
		opcion = messagebox.askquestion("Salir", "Desea salir de la aplicacion????", icon='warning')
		if opcion == "yes":
			self.raiz.destroy()
	
	def genReporte(self,datosaCsv):
		try:	
			listdata=self.cuadroguardar.get()
			print(listdata)
			if(listdata!=""):
				for row in self.datosaCsv:
					self.writeCSV_new(row,listdata)
				messagebox.showinfo("GenReportes", "Archivo CSV Generado OK")
				self.raiz.destroy()
			else:
				messagebox.showwarning("GenReportes", "Falta path paar Generar Reporte")
		except:
			messagebox.showwarning("GenReportes","Failed to genReporte TO csv")

##############################################################################################

def VisualizarArticulosaVender():
	ventana=ModuloVentas()

def consultarVentas():
	ventana=ModuloVentasGenerales()

def VisualizarReportes():
	misVentas=Ventas()
	reportes=ModuloReportes(misVentas.consultarVentas())

def VizualizarVentasporCliente():
	ventasPorCliente=ModuloConsultasVentas()

#########################################MENU PRINCIPAL##############################

def ventana_principal():
	global ventana
	ventana=Tk()
	ventana.geometry("600x500+450+100")
	ventana.title("------------Bienvenido!!------------")
	ventana.configure(background="white")
	'''Label(ventana,text="Sistema de ventas",fg="black",bg="white"font=("Times New Roman",10)).place(x=180,y=20'''



	menu_horizontal=Menu(ventana)

##############################MENU articulo##############################
	articulo=Menu(menu_horizontal,tearoff=0) #saca la linea de puntos del listado de menus
	articulo.add_command(label="Ingresar",command=articulo_ingresar)
	articulo.add_separator()
	articulo.add_command(label="Modificar",command=articulo_modificar)
	articulo.add_separator()
	articulo.add_command(label="Consultar",command=articulo_consultar)
	articulo.add_separator()
	articulo.add_command(label="Eliminar",command=articulo_eliminar)

	menu_horizontal.add_cascade(label="Articulo",menu=articulo)

	ventana.config(menu=menu_horizontal)

##############################MENU Cliente##############################
	Cliente=Menu(menu_horizontal,tearoff=0)
	Cliente.add_command(label="Ingresar",command=Cliente_ingresar)
	Cliente.add_separator()
	Cliente.add_command(label="Modificar",command=Cliente_modificar)
	Cliente.add_separator()
	Cliente.add_command(label="Consultar",command=Cliente_consultar)
	Cliente.add_separator()
	Cliente.add_command(label="Eliminar",command=Cliente_eliminar)

	menu_horizontal.add_cascade(label="Cliente",menu=Cliente)

	ventana.config(menu=menu_horizontal)

#############################Menu Ventas#################################
	Ventas=Menu(menu_horizontal,tearoff=0)
	Ventas.add_command(label="Vender",command=VisualizarArticulosaVender)
	Ventas.add_command(label="Consultar Ventas",command=consultarVentas)
	Ventas.add_command(label="Ventas por Cliente",command=VizualizarVentasporCliente)
	Ventas.add_separator()
	Ventas.add_command(label="Generar Reportes",command=VisualizarReportes)

	menu_horizontal.add_cascade(label="Ventas",menu=Ventas)
	ventana.config(menu=menu_horizontal)
	  
##############################MENU SALIR##############################
	m_salir=Menu(menu_horizontal,tearoff=0)
	menu_horizontal.add_cascade(label="Salir",command=ventana.destroy)
	ventana.config(menu=menu_horizontal)
	mainloop()


ventana_principal()