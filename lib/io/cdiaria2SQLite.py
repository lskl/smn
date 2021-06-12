## ----------------------------------------------------------------
## Leer algunas estaciones desde el directorio de datos
## primarios y añadirlos a la base de datos de SQLite
## ----------------------------------------------------------------

# -----------------------------------
# Funciones
# -----------------------------------

def crear_sqlite( ):

    from os.path import join
    import sqlite3

    # -*- coding: utf-8 -*-
    """
    Created on Thu May 13 19:57:16 2021

    @author: jcastillo
    """

    import sqlite3

    conexion = sqlite3.connect( join(dir_sqlite, "cdiaria.db") )

    try:
        conexion.execute("""
            create table estacion (
            numero integer primary key,
            nombre text,
            estado text,
            municipio text,
            situacion text,
            organismo text,
            cve text,
            latitud real,
            longitud real,
            altitud real
            )
            """)
        print("Se creo la tabla estacion")

    except sqlite3.OperationalError:
        print("La tabla ya existe")

    conexion.close()

    return 0


# -----------------------------------
# Main: para cuando se ejecute este script directamente
# -----------------------------------
if __name__ == "__main__":

    from cdiaria import *

    archivos = lista_archivos( dir_datos )
    archivos = archivos[:5]

    print( archivos ) # Para probar

    crear_sqlite()

    print('***')