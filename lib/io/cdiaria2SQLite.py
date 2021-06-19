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
            cve_omm text,
            latitud real,
            longitud real,
            altitud real,
            emision text)
            """)
        print("Se creó la tabla estación")

    except sqlite3.OperationalError:
        print("La tabla estaciones ya existe")

    try:
        conexion.execute("""
            create table datos_diarios (
            numero_estacion integer,
            dia integer,
            mes integer,
            anyo integer,
            precipitacion double,
            evaporacion double,
            temp_max double,
            temp_min double,
            primary key( numero_estacion, dia, mes, anyo )
            )
            """)
        print("Se creo la tabla datos_diarios")

    except sqlite3.OperationalError:
        print("La tabla datos_diarios ya existe")
    conexion.close()

    return 0

def insertar_en_tabla_estacion( conexion, registro, verbose=False ):

    try:
        # columnas = ['numero', 'nombre', 'estado', 'municipio', 'situacion', \
        #             'organismo', 'cve', 'latitud', 'longitud', 'altitud', 'emision']
        # conexion.executemany("""insert into estacion (?,?)""",
        #                      [(c, registro[c]) for c in columnas])


        sql_insert = """
            insert into estacion (
            numero, nombre, estado, municipio, situacion,
            organismo, cve_omm, latitud, longitud, altitud, emision
            )
            values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')
            """.format(
            registro['numero'], registro['nombre'], registro['estado'],
            registro['municipio'], registro['situacion'], registro['organismo'],
            registro['cve'], registro['latitud'], registro['longitud'],
            registro['altitud'], registro['emision'])

#        print( sql_insert )

        conexion.execute( sql_insert )
        if verbose:
            print("Registro añadido a la tabla Estaciones")

    except sqlite3.OperationalError:
        print("Error: No se pudo añadir el registro en la tabla Estaciones")
    except sqlite3.IntegrityError:
        if verbose:
            print('-' * 30)
            print(sql_insert)
            print( "Error de integridad de datos. ¿Ya estaba el registro en la tabla 'estacion'?" )
            print('-' * 30)
        else:
            pass
    return 0

def insertar_en_tabla_datos_diarios( conexion, datos, verbose=False ):

    import pandas as pd

    for index, row in datos.iterrows():


        try:
            # columnas = ['numero', 'nombre', 'estado', 'municipio', 'situacion', \
            #             'organismo', 'cve-omm', 'latitud', 'longitud', 'altitud']
            # conexion.executemany("""insert into estacion (?,?)""",
            #                      [(c, registro[c]) for c in columnas])

            sql_insert = """
                insert into datos_diarios (
                numero_estacion, dia, mes, anyo, precipitacion,
                evaporacion, temp_max, temp_min
                )
                values('{}','{}','{}','{}','{}','{}','{}','{}')
                """.format(
                row['Estacion'], row['Dia'], row['Mes'],
                row['Anyo'], row['Precipitacion'], row['Evaporacion'],
                row['T_max'], row['T_min'])
            # print( sql_query )
            conexion.execute( sql_insert )
            if verbose:
                print("Registro añadido a la tabla Estaciones")

        except sqlite3.OperationalError:
            print("Error: No se pudo añadir el registro")
        except sqlite3.IntegrityError:
            if verbose:
                print('-'*30)
                print( sql_insert )
                print( "Error de integridad de datos. ¿Ya estaba el registro en la tabla 'datos_diarios'?" )
                print('-' * 30)
            else:
                pass

    return 0


# -----------------------------------
# Main: para cuando se ejecute este script directamente
# -----------------------------------
if __name__ == "__main__":

    from cdiaria import *
    from os.path import join
    from time import time

    start = time()

    print('*'*50)
    print( 'Creando tablas en la base de datos cdiaria...' )
    crear_sqlite()
    print('*'*50)
    print(dir_datos)
    archivos = lista_archivos( dir_datos )
#    archivos = archivos[66:67]
    archivos = [a for a in archivos if "10066" in a]
    # print( archivos ) # Para probar

    # ------------------
    # Para cada archivo en la lista, leer el encabezado
    # e incluirlo en la tabla de estaciones de SQLite
    import sqlite3
    conexion = sqlite3.connect(join(dir_sqlite, "cdiaria.db"))

    print( 'Número de archivos en la lista:', len(archivos) )
    print('*'*50)
    for i, arch in enumerate(archivos):
        print( 'Procesando archivo #'+ str(i).zfill(5)+ ': ',arch, '...', end='' )
        encabezado,n = leer_smn_encabezado( join(dir_datos, arch) )
        insertar_en_tabla_estacion( conexion, encabezado, verbose=False )

        datos = leer_smn_mediciones( join(dir_datos, arch),n )

        insertar_en_tabla_datos_diarios( conexion, datos, verbose=False )
        print('\t → ok!')
    print('*'*50)

    conexion.commit()
    conexion.close()
# ------------------

    print( 'Fin' )
    print( 'Tiempo total de ejecución: ', time()-start, 'segundos' )
    print('*'*50)