import sqlite3
import hashlib
import sys

db = sqlite3.connect(':memory:') # Base de datos en memoria
def cifrar_password(password):
   cifrado = hashlib.sha512(password.encode('utf-8')).hexdigest()
   return cifrado

#db = sqlite3.connect('data/libro') # Base de datos en un archivo
#cursor= db.cursor()
#print("base de datos creada con exito")

#cursor.execute('''CREATE TABLE libro(id INTEGER PRIMARY KEY,
#                autor TEXT, publicacion INT, cantidad_pagina INT, isbn INT)''')
#print("Tabla creada con exito")

def agregar():
      while True:
          try:
              id = int(input("id: "))
              break
          except ValueError:
              print("oops! eso NO es Valido.!..intente de nuevo..")
      while True:
          try:
              autor = input("autor: ")
              break
          except RuntimeError:
              print("opps!.. eso NO es Valido.!..intente de nuevo..")
      while True:
           try:
               publicacion = int(input("publicacion de libro"))
               break
           except ValueError:
               print("opps!.. eso NO es Valido.!..intente de nuevo..")
      while True:
           try:
               cantidad = int(input("cantidad de paginas.."))
               break
           except ValueError:
               print("opps!.. eso NO es Valido.!..intente de nuevo..")
      while True:
          try:
              isbn = int(input("isbn"))
              break
          except ValueError:
              print("opps!.. eso NO es Valido.!..intente de nuevo..")
      db = sqlite3.connect('data/libro')
      cursor = db.cursor()
      cursor.execute("""INSERT INTO libro(id, autor, publicacion, cantidad_pagina, isbn) VALUES (?,?,?,?,?)""",
                     (id, autor, publicacion, cantidad, isbn))
      db.commit()
      db.close()
      input("pulse para continuar")
      menu()

def ver_libro():
    db = sqlite3.connect('data/libro')
    cursor = db.cursor()
    cursor.execute('''SELECT id, autor, publicacion, cantidad_pagina, isbn FROM libro''')
    for fila in cursor:
        print("id: {0}  autor: {1} publicacion de libro: {2} cantidad_paginas: {3} isbn: {4}".format(fila[0], fila[1], fila[2], fila[3], fila[4]))
    db.close()
    menu()

def eliminar():
    db = sqlite3.connect('data/libro')
    cursor = db.cursor()
    cursor.execute("SELECT * from libro")
    print("agregadas..")
    for fila in cursor:
        print("id: {0}  autor: {1} publicacion de libro: {2} cantidad_paginas: {3} isbn: {4}".format(fila[0], fila[1], fila[2], fila[3],fila[4]))
    while True:
        try:
            id = int(input("ID de libro a eliminar: "))
            break
        except ValueError:
             print("opps!.. eso NO es Valido.!..intente de nuevo..")

    cursor.execute("select * from libro")
    for fila in cursor:
        if int(id) == int(fila[0]):
            print("borrado..")
            cursor.execute('''DELETE FROM libro WHERE id = ?''',
                               (id,))
            db.commit()
            db.close()
            input("pulse para continuar")
            menu()

def modificar():
    db = sqlite3.connect('data/libro')
    cursor = db.cursor()
    cursor.execute("SELECT * from libro")
    for fila in cursor:
        print("id: ", fila[0])
        print("autor: ", fila[1])
        print("fecha de publicacion: ", fila[2])
        print("isbn: ", fila[3])
        print("///////////////////////////////////////////////////")
    while True:
        try:
            id = int(input("ID del libro a modificar: "))
            break
        except ValueError:
            print("opps!.. eso NO es Valido.!..intente de nuevo..")
    if int(id) == int(fila[0]):
        nuevo_autor = input(" Nuevo autor: ")
        while True:
            try:
                nueva_publicacion = int(input("nueva publicacion "))
                break
            except ValueError:
                print("oops! eso NO es Valido.!..intente de nuevo..")
        while True:
            try:
                nueva_cantidad = int(input("nueva cantidad de pagina "))
                break
            except ValueError:
                print("oops! eso NO es Valido.!..intente de nuevo..")
        while True:
            try:
                nuevo_isbn = int(input("nuevo isbn "))
                break
            except ValueError:
                print("oops! eso NO es Valido.!..intente de nuevo..")

        cursor.execute('''UPDATE libro SET autor=?, publicacion=?, cantidad_pagina=?, isbn = ? WHERE
                                           id = ?''', (nuevo_autor, nueva_publicacion, nueva_cantidad, nuevo_isbn,id))
        db.commit()
        db.close()
    print ("\nActualizada correctamente..")
    input("pulse para continuar..")
    menu()

def menu():
    while True:
        print("////////////////////MENU////////////////////")
        print("1: agregar..")
        print("2: ver libro..")
        print("3: Eliminar")
        print("4: Modificar")
        print("5: Salir")
        while True:
            try:
                seleccionar = int(input("selecciona un menu: "))
                break
            except ValueError:
                print("opps!.. eso NO es Valido.!..intente de nuevo..")

        if seleccionar == 1:
            agregar()
        elif seleccionar == 2:
            ver_libro()
        elif seleccionar == 3:
            eliminar()
        elif seleccionar == 4:
            modificar()
        elif seleccionar == 5:
            print("adios..")
            input()
            sys.exit()
        else:
            input("digite una opcion valida..")
            menu()
menu()



