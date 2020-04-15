from tkinter import *
from tkinter import ttk
from tkinter.ttk import Style
from tkinter import messagebox
from clasess import *
import tkinter as tk
import time

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


def VisualizarVentas():
    windowsVender=tk.Tk()
    windowsVender.title("Venta de Productos")
            
    articulosTotal=Articulos()

    miFrame_1 = Frame(windowsVender)
    miFrame_1.pack()

    tituloLabel=Label(miFrame_1,text="Articulos",fg="blue",bg="white",font=("Times New Roman",20))
    tituloLabel.grid(row=0, column=1,sticky="we",columnspan=6)

    botonVender = Button(miFrame_1, text="VENDER",width=15,command=lambda:realizarVenta())
    botonVender.grid(row=1, column=4,sticky="we")

    botonCancelar = Button(miFrame_1, text="CANCELAR VENTA",width=15)
    botonCancelar.grid(row=2, column=4,sticky="we")
     
    datacuadroCliente = StringVar()
    datacuadroUsuario = StringVar()
    datacuadroCantidad = IntVar()
    datacuadroEstado = StringVar()

    cuadroCliente = Entry(miFrame_1, textvariable=datacuadroCliente)
    cuadroCliente.grid(row=1, column=1, padx=10, pady=10)
    cuadroCliente.config(justify="center")

    cuadroUsuario = Entry(miFrame_1, textvariable=datacuadroUsuario)
    cuadroUsuario.grid(row=2, column=1, padx=10, pady=10)
    cuadroUsuario.config(justify="center")

    cuadroCantidad = Entry(miFrame_1, textvariable=datacuadroCantidad)
    cuadroCantidad.grid(row=1, column=3, padx=10, pady=10,)
    cuadroCantidad.config(justify="center")

    cuadroEstado = Entry(miFrame_1, textvariable=datacuadroEstado)
    cuadroEstado.grid(row=2, column=3, padx=10, pady=10,)
    cuadroEstado.config(justify="center")

    cuadroClienteLabel = Label(miFrame_1, text="Cliente: ")
    cuadroClienteLabel.grid(row=1, column=0, padx=10, pady=10)

    cuadroUsuarioLabel = Label(miFrame_1, text="Usuario: ")
    cuadroUsuarioLabel.grid(row=2, column=0, padx=10, pady=10)

    cuadroCantidadLabel = Label(miFrame_1, text="Cantidad: ")
    cuadroCantidadLabel.grid(row=1, column=2, padx=10, pady=10)

    cuadroEstadoLabel = Label(miFrame_1, text="Estado: ")
    cuadroEstadoLabel.grid(row=2, column=2, padx=10, pady=10)

    miFrame_2 = Frame(windowsVender)
    miFrame_2.pack()

    tree = ttk.Treeview(miFrame_2,columns = ("id_articulo","descripcion","codigo","stock","precio_vta"))   
    tree.grid(row=1,column=3,padx=10,pady=10)
            
    tree['show']='headings'
    tree.heading('#0', text='column0', anchor=tk.W)
    tree.heading('#1', text='id_articulo', anchor=tk.W)
    tree.heading('#2', text='descripcion', anchor=tk.W)
    tree.heading('#3', text='codigo', anchor=tk.W)
    tree.heading('#4', text='stock', anchor=tk.W)
    tree.heading('#5', text='precio_vta', anchor=tk.W)

    tree.column('#0',width=150,minwidth=100,stretch=tk.YES)
    tree.column('#1',width=150,minwidth=100,stretch=tk.YES)
    tree.column('#2',width=150,minwidth=100,stretch=tk.YES)
    tree.column('#3',width=150,minwidth=100,stretch=tk.YES)
    tree.column('#4',width=150,minwidth=100,stretch=tk.YES)
    tree.column('#5',width=150,minwidth=100,stretch=tk.YES)
            #tree.grid(row=5, column=5,sticky="nsew")

    for row in articulosTotal.consultar():
        tree.insert('',END, values=row) 
            
    miFrame_3 = Frame(windowsVender)
    miFrame_3.pack()
    ventasTotal=Ventas()

    tituloLabel=Label(miFrame_3,text="Ventas",fg="blue",bg="white",font=("Times New Roman",20))
    tituloLabel.grid(row=0, column=1, padx=10, pady=10,sticky="we")

    treeVentas = ttk.Treeview(miFrame_3,columns = ("id_articulo","descripcion","codigo","stock","precio_vta"))   
    treeVentas.grid(row=1,column=1,padx=10,pady=10)
            
    treeVentas['show']='headings'
    treeVentas.heading('#0', text='column0', anchor=tk.W)
    treeVentas.heading('#1', text='id_articulo', anchor=tk.W)
    treeVentas.heading('#2', text='descripcion', anchor=tk.W)
    treeVentas.heading('#3', text='codigo', anchor=tk.W)
    treeVentas.heading('#4', text='stock', anchor=tk.W)
    treeVentas.heading('#5', text='precio_vta', anchor=tk.W)

    treeVentas.column('#0',width=150,minwidth=100,stretch=tk.YES)
    treeVentas.column('#1',width=150,minwidth=100,stretch=tk.YES)
    treeVentas.column('#2',width=150,minwidth=100,stretch=tk.YES)
    treeVentas.column('#3',width=150,minwidth=100,stretch=tk.YES)
    treeVentas.column('#4',width=150,minwidth=100,stretch=tk.YES)
    treeVentas.column('#5',width=150,minwidth=100,stretch=tk.YES)
            #tree.grid(row=5, column=5,sticky="nsew")
        
    for row in ventasTotal.consultarVentas():
        treeVentas.insert('',END, values=row) 
            
            #tree.bind("<Double-1>", OnDoubleClick)

    windowsVender.mainloop()

def leerInfoInputBox():
    listadata = [datacuadroCliente.get(), datacuadroUsuario.get(),datacuadroCantidad.get(),datacuadroEstado.get()]
    print ("++++++++"+datacuadroCliente.get())
    return listadata

def borrarInputBox():
    datacuadroCliente.set("")
    datacuadroUsuario.set("")
    datacuadroCantidad.set(0)
    datacuadroEstado.set("")
        
    print("CRUDPy - Se borran todos los campos")


    #def OnDoubleClick(, event):
     #   item = tree.identify('item',event.x,event.y)
      #  print("you clicked on itemID: ", tree.item(item,"values")[0])
       # return tree.item(item,"values")[0]

    #def InsertarArticulos(,data):
    #    for row in data:
      #     tree.insert('',END, values=row) 

def realizarVenta():
    
    listadata=leerInfoInputBox()
    print("+++"+listadata[0] + listadata[1] + listadata[3])
    if(listadata[0]=="" or listadata[1]=="" or listadata[2]==0 or listadata[3]==""):
            #borrarInputBox()
        print(listadata[0] + listadata[1] + listadata[3])
        messagebox.showwarning("Ventas", "Error en los datos")
    else:
        item = tree.focus()
        idArticulo=tree.item(item,"values")[0]
        valorVenta=float(tree.item(item,"values")[4])*2
        print (tree.item(item,"values")[0])
            
        miTupla=(idArticulo,listadata[0],listadata[1],time.strftime("%d/%m/%y"),
                time.strftime("%H:%M:%S"),valorVenta*listadata[2],listadata[3])
        print(miTupla)
   


##############################################################################################




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
    articulo=Menu(menu_horizontal)
    articulo.add_command(label="Ingresar",command=articulo_ingresar)
    articulo.add_separator()
    articulo.add_command(label="Modificar",command=articulo_modificar)
    articulo.add_separator()
    articulo.add_command(label="Consultar",command=articulo_consultar)
    articulo.add_separator()
    articulo.add_command(label="Eliminar",command=articulo_eliminar)
    menu_horizontal.add_cascade(label="articulo",menu=articulo)
    ventana.config(menu=menu_horizontal)

    ##############################MENU Cliente##############################
    Cliente=Menu(menu_horizontal)
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
    Ventas=Menu(menu_horizontal)
    Ventas.add_command(label="Vender",command=VisualizarVentas)
    Ventas.add_separator()
    menu_horizontal.add_cascade(label="Ventas",menu=Ventas)
    ventana.config(menu=menu_horizontal)
  




    

    ##############################MENU SALIR##############################
    m_salir=Menu(menu_horizontal)
    menu_horizontal.add_cascade(label="SALIR",command=ventana.destroy)
    ventana.config(menu=menu_horizontal)
    mainloop()


ventana_principal()



