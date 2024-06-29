import os
import pandas as pd
import numpy as np
import glob
Datos_red_completa = pd.read_csv('/home/aaron/Descargas/Contenido/Resultados_Acanthospermum Australe/Filtrado_0.1/Para_cytoscape.csv')

#Funcion que transforme datos para que puedan compararse
def peine():
        directorio = '/home/aaron/Escritorio/cluster_acanthospermum/'
        archivos = glob.glob(os.path.join(directorio + "/*.csv")) 
        for f in archivos:
                data = pd.read_csv(f)
                print(data.columns)
                #data = data.rename(columns={data.columns[1]: 'Uniprot ID'})
                columnas = data[['Uniprot ID', 'MCODE::Score (1)']]

        return
print(peine())








# Funcion que abre todos los archivos de un directorio y los lee
# def scouter():
#     directorio = '/home/aaron/Escritorio/cluster_acanthospermum/'
#     archivos = glob.glob(os.path.join(directorio + "/*.csv")) # lista de todos los archivos en el directorio que contengan .csv
#     for f in archivos: # Para cada archivo individual dentro del cluster seleccionado con glob...
#         data = pd.read_csv(f) # Pandas lee individualmente cada archivo
#         alfa = pd.read_csv('/home/aaron/Descargas/Contenido/Resultados_Acanthospermum Australe/Filtrado_0.1/Para_cytoscape.csv')

#         #columnas = data[['stringdb::canonical name','MCODE::Score (1)']]
#     return    
    #df['col1'].equals(df['col2'])
# print(scouter())