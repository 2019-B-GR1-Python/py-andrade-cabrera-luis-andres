#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 07:58:24 2019

@author: andres
"""
import pandas as pd
import numpy as np
import os
import sqlite3
### Need packages openpyxl, xlsxwriter
path_save_full_bin = "/home/andres/Dropbox/6to&7moSemestre/IDW/py-andrade-cabrera-luis-andres/03-Pandas/data/artwork_data_full.pickle"
df5 = pd.read_pickle(path_save_full_bin)
df = df5.iloc[49980:50519,:].copy()
# tipos de archivos
# json
# excel
# sql

### EXCEL ###
df5.to_excel('data/mi_df_completo.xlsx')
path_guardado = 'data/mi_df_part.xlsx'
df.to_excel(path_guardado, index = False)
columnas = ['artist', 'title', 'year']
df.to_excel(path_guardado, columns = columnas) # Seleccion de las columnas

### Multiples hojas de trabajo ###
path_multiples = 'data/mi_df_multiples.xlsx'
writer = pd.ExcelWriter(path_multiples, engine='xlsxwriter')

df.to_excel(writer, sheet_name = 'Primera')
df.to_excel(writer, sheet_name = 'Segunda', index = False)
df.to_excel(writer, sheet_name = 'Tercera', columns = columnas)

writer.save() # Si no se utiliza el excel permanece solo en memoria

#num_artistas = df['artist'].value_counts()
num_artistas = df
path_colores = 'data/mi_df_colores.xlsx'

writer_colores = pd.ExcelWriter(path_colores, engine='xlsxwriter')

num_artistas.to_excel(writer_colores, sheet_name ='Artistas')

hoja_artistas = writer_colores.sheets['Artistas']
rango_celdas = 'B2:B{}'.format(len(num_artistas.index) + 1)

formato_artistas = {
        "type":"2_color_scale",
        "min_value":"10",
        "min_type":"percentile",
        "max_value": "99",
        "max_type":"percentile"}

hoja_artistas.conditional_format(rango_celdas, formato_artistas)

writer_colores.save()


### GRAFICAS ####
#workbook = xlsxwriter.Workbook(path_colores)
df.to_excel(writer_colores, sheet_name = 'Graficos', columns = columnas)
workbook = writer_colores.book
worksheet = workbook
chart = workbook.add_chart({'type': 'line'})
# Add a series to the chart.
chart.add_series({'values': '=Sheet2!$D$2:$D$200',
    'marker': {
        'type': 'square',
        'size': 8,
        'border': {'color': 'black'},
        'fill':   {'color': 'red'},
    },
})

# Insert the chart into the worksheet.
hoja_artistas.insert_chart('C2', chart)

workbook.close()