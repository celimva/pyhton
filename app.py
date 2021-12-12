import tkinter
from tkinter import *
from tkinter import ttk
from entregable4 import *
from entregable5 import *

def formulario():
    conexion = conectar_bbdd()
    cursor = conexion.cursor()
    insert = "INSERT INTO pegatina VALUES"
    cursor.execute(insert)
    lista = []
    for element in cursor.fetchall():
        pegatina = dic_pegatina.copy()
        pegatina['id'] = element
        pegatina['imagen'] = element
        pegatina['nombre'] = element
        pegatina['autor'] = element
        pegatina['precio'] = element
        lista.append(pegatina)


def mostrar_formulario():
    ventana_principal = Tk()
    ventana_principal.config(width=700, height=800)
    form = Frame(ventana_principal)

    titulo = Label(form, text="NUEVA PEGATINA")
    titulo.grid(row=0, column=1)
    titulo.config(font= ('Times New Roman', 18))

    nombre_label = Label(form, text="Nombre")
    nombre_label.grid(row= 1, column= 0)
    nombre_label.config(padx=10, pady=10)
    cuadro_nombre= Entry(form)
    cuadro_nombre.grid(row= 1, column= 2)

    url_label = Label(form, text="URL")
    url_label.grid(row=2, column=0)
    url_label.config(padx=10, pady=10)
    cuadro_url = Entry(form)
    cuadro_url.grid(row=2, column=2)

    autor_label = Label(form, text="Autor")
    autor_label.grid(row=3, column=0)
    autor_label.config(padx=10, pady=10)
    cuadro_autor = Entry(form)
    cuadro_autor.grid(row=3, column=2)

    precio_label = Label(form, text="Precio")
    precio_label.grid(row=4, column=0)
    precio_label.config(padx=10, pady=10)
    cuadro_precio = Entry(form)
    cuadro_precio.grid(row=4, column=2)

    boton= Button(form, text= "Insertar", command= lambda:insertar_pegatina(cuadro_nombre.get(), cuadro_url.get(), cuadro_autor.get(), cuadro_precio.get()))
    boton.grid(row= 5, column=1)

    form.pack()
    ventana_principal.mainloop()



def eliminar_pegatina():
    ventana = Tk()
    ventana.config(width=900, height=800)
    form2 = Frame(ventana)

    tit = Label(form2, text="¿Cuál es el nombre de la pegatina que quieres eliminar?")
    tit.grid(row=0, column=1)
    tit.config(font= ('Times New Roman', 18))

    nombre_label = Label(form2, text="Nombre")
    nombre_label.grid(row=1, column=0)
    nombre_label.config(padx=10, pady=10)
    cuadro_nombre2 = Entry(form2)
    cuadro_nombre2.grid(row=1, column=2)

    bot = Button(form2, text="Eliminar",command=lambda: eliminar_elemento(cuadro_nombre2.get()))
    bot.grid(row=2, column=1)

    form2.pack()
    ventana.mainloop()

def obtener_todas_las_pegatinas():
    conexion = conectar_bbdd()
    cursor = conexion.cursor()
    script = "SELECT * from pegatina  "
    cursor.execute(script)
    lista=[]
    for element in cursor.fetchall():
        pegatina= dic_pegatina.copy()
        pegatina['id'] = element[0]
        pegatina['imagen'] = element[1]
        pegatina['nombre'] = element[2]
        pegatina['autor'] = element[3]
        pegatina['precio'] = element[4]
        lista.append(pegatina)

    cerrar_conexion(conexion)
    return lista



def mostrar_tabla():
    pegatinas = obtener_todas_las_pegatinas()
    linea = 1


    ventana_principal = Tk()
    ventana_principal.pack_slaves()
    tabla = ttk.Treeview(ventana_principal)
    tabla['columns'] = ("id","imagen", "nombre" ,"autor", "precio")
    tabla.column("#0", width=0, stretch=NO)
    tabla.column("id",anchor=CENTER, width=100)
    tabla.column("imagen", anchor=CENTER, width=200)
    tabla.column("nombre", anchor=CENTER, width=200)
    tabla.column("autor", anchor=CENTER, width=200)
    tabla.column("precio", anchor=CENTER, width=100)

    tabla.heading("#0", text="", anchor=CENTER)
    tabla.heading("id", text="id", anchor=CENTER)
    tabla.heading("imagen", text="imagen", anchor=CENTER)
    tabla.heading("nombre", text="nombre", anchor=CENTER)
    tabla.heading("autor", text="autor", anchor=CENTER)
    tabla.heading("precio", text="precio", anchor=CENTER)

    index = 1
    for pegatina in pegatinas:
        tabla.insert(parent="", index=index, values=(pegatina["id"], pegatina["imagen"], pegatina["nombre"], pegatina["autor"], pegatina["precio"]))
        index +=1

    tabla.pack()
    tabla.mainloop()

def lanzar_aplicacion():
    ventana_principal = Tk()
    ventana_principal.config(width= 900, height= 1000)
    menu_principal = Menu(ventana_principal)
    ventana_principal.config(menu = menu_principal)
    ventana_principal.configure(bg= '#7D80DA')
    ventana_principal.title("El mundo de las pegatinas")



    # submenu Mostrar palas
    mostrar = Menu(menu_principal, tearoff=0)
    menu_principal.add_cascade(menu=mostrar, label="Mostrar")
    mostrar.add_command(label="pegatinas", command= lambda: mostrar_tabla())


    #submenu cargar palas
    sub_menu = Menu(menu_principal, tearoff= 0)
    menu_principal.add_cascade(menu=sub_menu, label= "Cargar")
    sub_menu.add_command( label="pegatinas", command=lambda: insertar_pegatinas())

    # submenu consultar palas
    consult = Menu(menu_principal, tearoff=0)
    menu_principal.add_cascade(menu=consult, label="Consulta")
    consult.add_command(label="pegatinas", command=lambda: consultar())

    # submenu eliminar palas
    delete = Menu(menu_principal, tearoff=0)
    menu_principal.add_cascade(menu=delete, label="Borrar")
    delete.add_command(label="pegatinas", command=lambda: borrar_datos())

    #submenu insertar palas
    insertar = Menu(menu_principal, tearoff=0)
    menu_principal.add_cascade(menu=insertar, label="Insertar")
    insertar.add_command(label="pegatinas", command=lambda: mostrar_formulario())

    # submenu insertar palas
    Eliminar = Menu(menu_principal, tearoff=0)
    menu_principal.add_cascade(menu=Eliminar, label="Eliminar")
    Eliminar.add_command(label="pegatinas", command=lambda: eliminar_pegatina())


    ventana_principal.mainloop()
lanzar_aplicacion()