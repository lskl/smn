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

def insertar_en_tabla_estacion( conexion, registro ):

    try:
        # columnas = ['numero', 'nombre', 'estado', 'municipio', 'situacion', \
        #             'organismo', 'cve', 'latitud', 'longitud', 'altitud']
        # conexion.executemany("""insert into estacion (?,?)""",
        #                      [(c, registro[c]) for c in columnas])

        sql_insert = """
            insert into estacion (
            numero, nombre, estado, municipio, situacion,
            organismo, cve, latitud, longitud, altitud
            )
            values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')
            """.format(
            registro['numero'], registro['nombre'], registro['estado'],
            registro['municipio'], registro['situacion'], registro['organismo'],
            registro['cve'], registro['latitud'], registro['longitud'],
            registro['altitud'])
        # print( sql_query )
        conexion.execute( sql_insert )
        print("Registro añadido a la tabla Estaciones")

    except sqlite3.OperationalError:
        print("Error: No se pudo añadir el registro")

    return 0


# -----------------------------------
# Main: para cuando se ejecute este script directamente
# -----------------------------------
if __name__ == "__main__":

    from cdiaria import *
    from os.path import join

    crear_sqlite()

    archivos = lista_archivos( dir_datos )
    archivos = archivos[:5]

    print( archivos ) # Para probar

    # ------------------
    # Para cada archivo en la lista, leer el encabezado
    # e incluirlo en la tabla de estaciones de SQLite
    import sqlite3
    conexion = sqlite3.connect(join(dir_sqlite, "cdiaria.db"))

    for arch in archivos:
        encabezado = leer_smn_encabezado( join(dir_datos, arch) )
        insertar_en_tabla_estacion( conexion, encabezado )
    conexion.close()
# ------------------


    print('Fin')