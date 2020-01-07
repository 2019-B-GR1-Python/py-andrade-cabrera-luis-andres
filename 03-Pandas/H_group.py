#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 09:19:03 2020

@author: andres
"""

import pandas as pd
import math
path_save_full_bin = "/home/andres/Dropbox/6to&7moSemestre/IDW/py-andrade-cabrera-luis-andres/03-Pandas/data/artwork_data_full.pickle"
df = pd.read_pickle(path_save_full_bin)

seccion_df = df.iloc[49980:50019,:].copy()

df_agrupado = seccion_df.groupby('artist')

type(df_agrupado)

for columna_agrupada, df_completo in df_agrupado:
    print(type(columna_agrupada))
    print(type(df_completo))

seccion_df['units'] #serie
a = seccion_df['units'].value_counts()
a.empty

def llenar_valores_vacios(series,tipo):
    lista_valores = series.value_counts()
    if(lista_valores.empty == True):
        return series
    else:
        if(tipo == 'promedio'):
            suma = 0
            numero_valores = 0
            for valor_serie in series:
                if(isinstance(valor_serie,str)):
                    valor = int(valor_serie)
                    numero_valores = numero_valores + 1
                    suma = suma + valor
            promedio = suma / numero_valores
            series_valores_llenos = series.fillna(promedio)
            return series_valores_llenos
        elif(tipo == 'frecuencia'):
            max = lista_valores.reset_index().head(1)['index'][0]
            series_valores_llenos = series.fillna(max)
            return series_valores_llenos
def transformar_df_promedio(df):
    df_artist = df.groupby('artist')
    lista_df=[]
    for artista, df in df_artist:
        copia = df.copy()
        serie_w = copia['width']
        serie_h = copia['height']
        copia.loc[:,'width'] = llenar_valores_vacios(serie_w,'promedio')
        copia.loc[:,'heigth'] = llenar_valores_vacios(serie_h,'promedio')
        lista_df.append(copia)
    df_completo_con_valores = pd.concat(lista_df)
    return df_completo_con_valores

def transformar_df_frecuencia(df):
    df_artist = df.groupby('artist')
    lista_df=[]
    for artista, df in df_artist:
        copia = df.copy()
        serie_w = copia['width']
        serie_h = copia['height']
        copia.loc[:,'width'] = llenar_valores_vacios(serie_w,'frecuencia')
        copia.loc[:,'heigth'] = llenar_valores_vacios(serie_h,'frecuencia')
        lista_df.append(copia)
    df_completo_con_valores = pd.concat(lista_df)
    return df_completo_con_valores
df_valores_llenos = transformar_df_frecuencia(seccion_df)
