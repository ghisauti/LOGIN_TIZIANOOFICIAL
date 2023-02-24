import tkinter
from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox as MessageBox


bd = sqlite3.connect("tizi.bd")
cur= bd.cursor()
cur.execute("SELECT ID FROM login")
resp= cur.fetchall()

def escribir():  
    nombre = caja1.get()
    apellido = caja2.get()
    edad = caja3.get()
    dni = caja4.get()
    sql='''INSERT INTO login (nombre, apellido, edad, dni)
    VALUES('{}', '{}', '{}', '{}')'''.format(nombre, apellido, edad, dni)
    cur.execute(sql)
    bd.commit()
    bd.close()
    
def buscar():
    id = lista_desplegable.get()
    query = "SELECT * FROM login WHERE ID ={}".format(id)
    cur.execute(query)
    datos = cur.fetchall()
    
    caja1.insert(0, datos[0][1])
    caja2.insert(0, datos[0][2])
    caja3.insert(0, datos[0][3])
    caja4.insert(0, datos[0][4])
    
    
def borrar():    
    caja1.delete(0,END)
    caja2.delete(0,END)
    caja3.delete(0,END)
    caja4.delete(0,END)
     
       
ventana = Tk()
ventana.resizable(0,0)
ventana.title ("TiziLogin")
ventana.geometry ("500x220+550+300")
Label(ventana, text = "Nombre:").pack()
caja1 = Entry(ventana)
caja1.pack()
Label(ventana, text = "Apellido").pack()
caja2 = Entry(ventana)
caja2.pack()
Label(ventana, text = "Edad:").pack()
caja3 = Entry(ventana)
caja3.pack()
Label(ventana, text = "Dni:").pack()
caja4 = Entry(ventana)
caja4.pack()
guardar = tkinter.Button (ventana, text= "Guardar", command = escribir)
guardar.pack()
guardar.place(x=340, y=169)

leer = tkinter.Button (ventana, text= "Buscar", command = buscar)
leer.pack()
leer.place(x=70, y=169)

borrar = tkinter.Button (ventana, text= "Borrar", command = borrar)
borrar.pack()
borrar.place(x=420, y=169)


#Lista Desplegable

lista_desplegable = ttk.Combobox(ventana,width=17)
lista_desplegable.place (x=170, y=169)

opciones = ["opcion 1","opcion 2","opcion 3",]
lista_desplegable['values']=resp




ventana.mainloop()