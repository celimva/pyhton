import mysql.connector as conector
from entregable4 import *



def conectar_bbdd():
    mi_conexion = conector.connect(host="localhost", port= "3306", user= "root", password= "1234", database="pegatinas_db",
                                   autocommit=True)
    return mi_conexion

def cerrar_conexion(conexion):
    conexion.close()

def consultar():
    conexion = conectar_bbdd()
    cursor = conexion.cursor()
    script = "SELECT * from pegatina  "
    cursor.execute(script)
    cerrar_conexion(conexion)
    return print(cursor.fetchall())

def insertar_pegatinas():
    list_pegatinas = cargar_elementos()
    conexion = conectar_bbdd()
    cursor = conexion.cursor()
    insert_script = "insert into pegatina ( imagen, nombre, autor, precio) values( %s, %s, %s, %s)"
    for pegatina in list_pegatinas:
        values = [pegatina["imagen"], pegatina["nombre"], pegatina["autor"], pegatina["precio"]]
        cursor.execute(insert_script, values)
    print("proceso terminado")

def insertar_pegatina(nombre, url, autor, precio):
    conexion = conectar_bbdd()
    cursor = conexion.cursor()
    insert_script = "insert into pegatina ( imagen, nombre, autor, precio) values( %s, %s, %s, %s)"
    cursor.execute(insert_script, [url, nombre, autor,precio])
    print("PEGATINA INSERTADA")


def borrar_datos():
    conexion = conectar_bbdd()
    cursor = conexion.cursor()
    borrar_script = "delete from pegatina"

    cursor.execute(borrar_script)
    print("PEGATINAS BORRADAS")

def eliminar_elemento(nombre):
    conexion = conectar_bbdd()
    cursor = conexion.cursor()
    drop = "delete from pegatina where nombre = %s"
    print(cursor.execute(drop, [nombre]))
    print("PEGATINA BORRADA")



