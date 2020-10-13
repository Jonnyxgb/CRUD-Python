from tkinter import *
from tkinter import messagebox
import sqlite3

root=Tk()

#----------------funciones---------------------

def conexionBBDD():

	miconexion=sqlite3.connect("Usuarios")

	Micursor=miconexion.cursor()

	try:

		Micursor.execute('''
			CREATE TABLE DATOSUSUARIOS(
			ID INTEGER PRIMARY KEY AUTOINCREMENT,
			NOMBRE_USUARIO VARCHAR(50),
			PASSWORD VARCHAR(50),
			APELLIDO VARCHAR(50),
			DIRECCION VARCHAR(50),
			COMENTARIOS VARCHAR(100))
			''')

		messagebox.showinfo("BBDD", "BBDD creada con exito")

	except:
		
		messagebox.showwarning("¡Atencion!", "La BBDD ya existe")

def salirAplicacion():
	
	valor=messagebox.askquestion("Salir", "deseas salir de la aplicacion")

	if valor=="yes":
		root.destroy()			

def limpiarCampos():

	miId.set("")
	miNombre.set("")
	miPass.set("")
	miApellido.set("")
	miDireccion.set("")
	textocomentario.delete(1.0, END)

def crear():

	miconexion=sqlite3.connect("Usuarios")

	Micursor=miconexion.cursor()

	Micursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,'" + miNombre.get() +
		"','" + miPass.get() + 
		"','" + miApellido.get() +
		"','" + miDireccion.get() +
		"','" + textocomentario.get("1.0", END) + "')")

	miconexion.commit()

	messagebox.showinfo("BBDD", "Registro ingresado con exito")

def leer ():

	miconexion=sqlite3.connect("Usuarios")

	Micursor=miconexion.cursor()

	Micursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID=" + miId.get())

	elUsuario=Micursor.fetchall()

	for usuario in elUsuario:

		miId.set(usuario[0])
		miNombre.set(usuario[1])
		miPass.set(usuario[2])
		miApellido.set(usuario[3])
		miDireccion.set(usuario[4])
		textocomentario.insert(1.0 ,usuario[5])

	miconexion.commit()

def actualizar():

	miconexion=sqlite3.connect("Usuarios")

	Micursor=miconexion.cursor()

	Micursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO='" + miNombre.get() +
		"', PASSWORD='" + miPass.get() + 
		"', APELLIDO='" + miApellido.get() +
		"', DIRECCION='" + miDireccion.get() +
		"', COMENTARIOS='" + textocomentario.get("1.0", END) +
		"' WHERE ID=" + miId.get())

	miconexion.commit()

	messagebox.showinfo("BBDD", "Registro actualizado con exito")

def eliminar():
	
	miconexion=sqlite3.connect("Usuarios")

	Micursor=miconexion.cursor()

	Micursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID=" + miId.get())

	miconexion.commit()	

	messagebox.showinfo("BBDD", "El registro se a eliminado con exito")

barramenu=Menu(root)
root.config(menu=barramenu, width=300, height=300)

bbddmenu=Menu(barramenu, tearoff=0)
bbddmenu.add_command(label="Conectar", command=conexionBBDD)
bbddmenu.add_command(label="Salir", command=salirAplicacion)

borrarmenu=Menu(barramenu, tearoff=0)
borrarmenu.add_command(label="Borrar Campos", command=limpiarCampos)

crudmenu=Menu(barramenu, tearoff=0)
crudmenu.add_command(label="Crear", command=crear)
crudmenu.add_command(label="Leer", command=leer)
crudmenu.add_command(label="Actualizar", command=actualizar)
crudmenu.add_command(label="Eliminar", command=eliminar)

ayudamenu=Menu(barramenu, tearoff=0)
ayudamenu.add_command(label="Licencia")
ayudamenu.add_command(label="Acerca de...")




barramenu.add_cascade(label="BBDD", menu=bbddmenu)
barramenu.add_cascade(label="Borrar", menu=borrarmenu)
barramenu.add_cascade(label="CRUD", menu=crudmenu)
barramenu.add_cascade(label="Ayuda", menu=ayudamenu)

#-------------Comienzo de campos---------------------

miframe=Frame(root)
miframe.pack()

miId=StringVar()
miNombre=StringVar()
miPass=StringVar()
miApellido=StringVar()
miDireccion=StringVar()


cuadroID=Entry(miframe, textvariable=miId)
cuadroID.grid(row=0, column=1, padx=10, pady=10)

cuadroNombre=Entry(miframe, textvariable=miNombre)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
cuadroNombre.config(fg="blue", justify="right")

cuadroPass=Entry(miframe, textvariable=miPass)
cuadroPass.grid(row=2, column=1, padx=10, pady=10)
cuadroPass.config(show="?")

cuadroApellido=Entry(miframe, textvariable=miApellido)
cuadroApellido.grid(row=3, column=1, padx=10, pady=10)

cuadroDireccion=Entry(miframe, textvariable=miDireccion)
cuadroDireccion.grid(row=4, column=1, padx=10, pady=10)

textocomentario=Text(miframe, width=16, height=5)
textocomentario.grid(row=5, column=1, padx=10, pady=10)
scrollVert=Scrollbar(miframe, command=textocomentario.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")

textocomentario.config(yscrollcommand=scrollVert.set)


#----------------Label----------------------

idLabel=Label(miframe, text="Id: ")
idLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

nombreLabel=Label(miframe, text="Nombre: ")
nombreLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

passLabel=Label(miframe, text="Pasword: ")
passLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

apellidoLabel=Label(miframe, text="Apellido: ")
apellidoLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

direccionLabel=Label(miframe, text="Direccion: ")
direccionLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

textoLabel=Label(miframe, text="Comentarios: ")
textoLabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)

#------------Botones-------------------

miframe2=Frame(root)
miframe2.pack()

botonCrear=Button(miframe2, text="Crear", command=crear)
botonCrear.grid(row=1, column=0, sticky="e", padx=10, pady=10)

botonRead=Button(miframe2, text="Leer", command=leer)
botonRead.grid(row=1, column=1, sticky="e", padx=10, pady=10)

botonUpdate=Button(miframe2, text="Actualizar", command=actualizar)
botonUpdate.grid(row=1, column=2, sticky="e", padx=10, pady=10)

botonDelete=Button(miframe2, text="Eliminar", command=eliminar)
botonDelete.grid(row=1, column=3, sticky="e", padx=10, pady=10)



root.mainloop()