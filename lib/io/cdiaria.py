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

# -----------------------------------
# Funciones
# -----------------------------------
def lista_archivos( directorio ):
    from os import listdir
    from os.path import join, isfile

    archivos = listdir( directorio )
    archivos = [ f for f in archivos if isfile( join(dir_datos, f) ) ]
    return sorted( archivos )

def leer_cdiaria( filename, path='' ):

# Comentario bobo para hacer un commit

    return 0

# -----------------------------------
# Main: para cuando se ejecute este script directamente
# -----------------------------------
if __name__ == "__main__":

#    print( lista_archivos( dir_datos ) ) # Para probar