import sqlite3
import hashlib
import sys

db = sqlite3.connect(':memory:') # Base de datos en memoria
db = sqlite3.connect('data/basededatos') # Base de datos en un archivo

cursor = db.cursor()
#cursor.execute('''CREATE TABLE persona(id INTEGER PRIMARY KEY,
#                 nombre TEXT, apellido TEXT, lugar_nacimiento TEXT, año_nacimiento INT )''')

#cursor.execute('''CREATE TABLE familia(id_padre INTEGER , id_hijo INTEGER,
#                                 FOREIGN KEY(id_padre) REFERENCES persona(id),
#                                 FOREIGN KEY(id_hijo) REFERENCES relacion(id_relacion) )''')

#cursor.execute('''CREATE TABLE relacion(id_relacion INTEGER PRIMARY KEY )''')

def agregar():
    while True:
        try:
            id = int(input("id: "))
            break
        except ValueError:
            print("oops! eso NO es Valido.!..intente de nuevo..")
    while True:
        try:
            nombre = input("nombre: ")
            break
        except ValueError:
            print("oops! eso NO es Valido.!..intente de nuevo..")
    while True:
        try:
            apellido = input("apellido: ")
            break
        except ValueError:
            print("oops! eso NO es Valido.!..intente de nuevo..")
    while True:
        try:
            lugar_nacimiento = input("lugar_nacimiento: ")
            break
        except ValueError:
            print("oops! eso NO es Valido.!..intente de nuevo..")
    while True:
        try:
            año_nacimiento = int(input("año_nacimiento: "))
            break
        except ValueError:
            print("oops! eso NO es Valido.!..intente de nuevo..")

    db = sqlite3.connect('data/basededatos')
    cursor = db.cursor()
    cursor.execute('''INSERT INTO persona(id, nombre, apellido, lugar_nacimiento, año_nacimiento) VALUES 
                      (?,?,?,?,?)''', (id, nombre, apellido, lugar_nacimiento, año_nacimiento))

    db.commit()
    db.close()
    input("pulse para continuar")
    menu()

def relacionar():
    while True:
        try:
            id_padre = int(input("id_padre: "))
            break
        except ValueError:
            print("oops! eso NO es Valido.!..intente de nuevo..")
    while True:
        try:
            id_hijo = int(input("id_hijo: "))
            break
        except ValueError:
            print("oops! eso NO es Valido.!..intente de nuevo..")

    db = sqlite3.connect('data/basededatos')
    cursor = db.cursor()
    cursor.execute('''INSERT INTO familia(id_padre, id_hijo) VALUES 
                         (?,?)''', (id_padre, id_hijo))

    db.commit()
    db.close()
    input("pulse para continuar")
    menu()

def ver_familia():
    db = sqlite3.connect('data/basededatos')
    cursor = db.cursor()
    cursor.execute('''SELECT * from persona, familia''')
    for fila in cursor:
        print("id: {0}  nombre: {1} apellido: {2} lugar_nacimiento: {3} año_nacimiento: {4} id_padre: {5} id_hijo: {6}".format(fila[0], fila[1],fila[2], fila[3], fila[4],  fila[5],  fila[6]))


    db.commit()
    db.close()
    input("pulse para continuar")
    menu()


def menu():
    while True:
        print("////////////////////MENU////////////////////")
        print("1: agregar personas..")
        print("2: establece..")
        print("3: ver familias")
        print("4: Salir")
        while True:
            try:
                seleccionar = int(input("selecciona un menu: "))
                break
            except ValueError:
                print("opps!.. eso NO es Valido.!..intente de nuevo..")

        if seleccionar == 1:
            agregar()
        elif seleccionar == 2:
            relacionar()
        elif seleccionar == 3:
            ver_familia()
        elif seleccionar == 4:
            print("adios..")
            input()
            sys.exit()
        else:
            input("digite una opcion valida..")
            menu()
menu()

