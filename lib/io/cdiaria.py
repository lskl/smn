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
import pandas as pd

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
    import re

    lista=[]
    campo=""
    with open(archivo, 'rb') as f:

        while(campo!="FECHA"):
            renglon=next(f).decode('latin-1')
            lista = lista+[renglon]
            campo = re.search(r"FECHA", renglon)
            if(campo):
                campo = campo.group()

    for renglon in lista:
        if(re.search(r"\AESTACI",renglon)):
            est_numero = int(renglon.split(':')[1])
        elif(re.search(r"\ANOMBRE",renglon)):
            est_nombre = renglon.split(':')[1].strip().strip('\n')
        elif(re.search(r"\AESTADO",renglon)):
            est_estado = renglon.split(':')[1].strip().strip('\n')
        elif(re.search(r"\AMUNICIPIO", renglon)):
            est_municipio = renglon.split(':')[1].strip().strip('\n')
        elif(re.search(r"\ASITUACI",renglon)):
            est_situacion = renglon.split(':')[1].strip().strip('\n')
        elif (re.search(r"\AORGANISMO", renglon)):
            est_organismo = renglon.split(':')[1].strip().strip('\n')
        elif(re.search(r"\ACVE-OMM",renglon)):
            est_cve = renglon.split(':')[1].strip().strip('\n')
        elif (re.search(r"\ALATITUD",renglon)):
            est_latitud = renglon.split(':')[1].strip().strip('\n')
        elif (re.search(r"\ALONGITUD",renglon)):
            est_longitud = renglon.split(':')[1].strip().strip('\n')
        elif(re.search(r"\AALTITUD",renglon)):
            est_altitud = renglon.split(':')[1].strip().strip('\n')
        elif (re.search(r"\AEMISION",renglon)):
            est_emision = renglon.split(':')[1].strip().strip('\n')

    est_latitud = est_latitud.split('°')[0]  # elimina "°"
    est_longitud = est_longitud.split('°')[0]  # elimina "°"
    est_altitud = est_altitud.split(' ')[0].replace(',', '')  # elimina " msnm"

    est_numero = int( est_numero )
    est_latitud = float(est_latitud)
    est_longitud = float(est_longitud)
    est_altitud = float(est_altitud)


        # print(est_numero, est_nombre, est_estado, est_municipio)
        # print(est_latitud, est_longitud, est_altitud)

#    print(len(lista))

    encabezado = {'numero': est_numero,
                      'nombre': est_nombre,
                      'estado': est_estado,
                      'municipio': est_municipio,
                      'situacion': est_situacion,
                      'organismo': est_organismo,
                      'cve': est_cve,
                      'latitud': est_latitud,
                      'longitud': est_longitud,
                      'altitud': est_altitud,
                      'emision': est_emision}

#    print(encabezado)

    return encabezado, len(lista)


def leer_smn_mediciones(archivo, n):
    import re

    est_numero = re.search(r"\d+",archivo).group()

    df = pd.read_fwf( archivo, skiprows=n )

    df.columns = ['Fecha', 'Precipitacion', 'Evaporacion', 'T_max', 'T_min']

    #    df = df[ df['Precipitacion'].str[0]!='-' ] # sí funciona
    #    df = df[ df['Precipitacion'].apply( lambda x: '-' not in x) ] # sí funciona
    mask = df['Precipitacion'].str.contains(r'-')
    df = df[~mask]

    mask = df['Fecha'].str.contains(r'\d\d/\d\d/\d\d\d\d', na=False)
    df = df[mask]

    df['Precipitacion'] = df['Precipitacion'].apply(pd.to_numeric, errors='coerce')
    df['Evaporacion'] = df['Evaporacion'].apply(pd.to_numeric, errors='coerce')
    df['T_max'] = df['T_max'].apply(pd.to_numeric, errors='coerce')
    df['T_min'] = df['T_min'].apply(pd.to_numeric, errors='coerce')

    # Versión para buscar errores
    # try:
    #     df['Dia'] = df['Fecha'].apply( lambda x: x.split('/')[0] )
    #     df['Mes'] = df['Fecha'].apply( lambda x: x.split('/')[1] )
    #     df['Anyo'] = df['Fecha'].apply( lambda x: x.split('/')[2] )
    # except Exception as e:
    #     print( e.__class__ )
    #     for index, row in df.iterrows():
    #         fecha = row['Fecha']
    #         try:
    #             dma = row['Fecha'].split('/')
    #             if len( dma )<3:
    #                 print( dma )
    #         except Exception as e:
    #             print( dma, type(dma) )
    #             print( e.__class__ )
    #             return 0

    df['Dia'] = df['Fecha'].apply(lambda x: x.split('/')[0])
    df['Mes'] = df['Fecha'].apply(lambda x: x.split('/')[1])
    df['Anyo'] = df['Fecha'].apply(lambda x: x.split('/')[2])

    df['Estacion'] = est_numero
    df = df[['Estacion', 'Dia', 'Mes', 'Anyo', 'Precipitacion', 'Evaporacion', 'T_max', 'T_min']]

    return df



def leer_cdiaria( filename, path='' ):

# Comentario bobo para hacer un commit

    return 0

# -----------------------------------
# Main: para cuando se ejecute este script directamente
# -----------------------------------
if __name__ == "__main__":

    print( '...' ) # Para probar
