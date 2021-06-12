## ----------------------------------------------------------------
## Funciones para leer los datos de los archivos de climatología
## diaria del servicio meteorológico nacional mexicano
## ----------------------------------------------------------------
## Funciones en este archivo:
## leer_cdiaria( filename, path='' )
## lista_archivos( directorio )
## ----------------------------------------------------------------
## 
## 
## ----------------------------------------------------------------
'''
leer_cdiaria()

Lee un archivo de texto con datos de climatología diaria de acuerdo
a la definición del Sistema Meteorológico Nacional Mexicano,
descrita en: 
https://smn.conagua.gob.mx/tools/RESOURCES/estacion/EstacionesClimatologicas.pdf

'''

# -----------------------------------
# Variables globales
# -----------------------------------
dir_datos = '../../../datos/datos primarios/Total de estaciones'
dir_sqlite = '../../../datos/db/sqlite'

# -----------------------------------
# Funciones
# -----------------------------------
def lista_archivos( directorio ):
    from os import listdir
    from os.path import join, isfile

    archivos = listdir( directorio )
    archivos = [ f for f in archivos if isfile( join(dir_datos, f) ) ]
    return sorted( archivos )


def leer_smn_encabezado(archivo):
    with open(archivo, 'rb') as f:
        next(f).decode('latin-1')
        next(f).decode('latin-1')
        next(f).decode('latin-1')
        next(f).decode('latin-1')

        est_numero = next(f).decode('latin-1')
        est_numero = int(est_numero.split(':')[1])
        est_nombre = next(f).decode('latin-1')
        est_nombre = est_nombre.split(':')[1].strip()
        est_estado = next(f).decode('latin-1')
        est_estado = est_estado.split(':')[1].strip()
        est_municipio = next(f).decode('latin-1')
        est_municipio = est_municipio.split(':')[1].strip()
        est_situacion = next(f).decode('latin-1')
        est_organismo = next(f).decode('latin-1')
        est_cve = next(f).decode('latin-1')
        est_latitud = next(f).decode('latin-1')
        est_latitud = est_latitud.split(':')[1].strip()
        est_latitud = est_latitud.split('°')[0]  # elimina "°"
        est_longitud = next(f).decode('latin-1')
        est_longitud = est_longitud.split(':')[1].strip()
        est_longitud = est_longitud.split('°')[0]  # elimina "°"
        est_altitud = next(f).decode('latin-1')
        est_altitud = est_altitud.split(':')[1].strip()
        est_altitud = est_altitud.split(' ')[0].replace(',', '')  # elimina " msnm"

        # print(est_numero, est_nombre, est_estado, est_municipio)
        # print(est_latitud, est_longitud, est_altitud)

        encabezado = {'numero': est_numero,
                      'nombre': est_nombre,
                      'estado': est_estado,
                      'municipio': est_municipio,
                      'situacion': est_situacion,
                      'organismo': est_organismo,
                      'cve': est_cve,
                      'latitud': est_latitud,
                      'longitud': est_longitud,
                      'altitud': est_altitud}
        return encabezado


def leer_cdiaria( filename, path='' ):

# Comentario bobo para hacer un commit

    return 0

# -----------------------------------
# Main: para cuando se ejecute este script directamente
# -----------------------------------
if __name__ == "__main__":

    print( '...' ) # Para probar