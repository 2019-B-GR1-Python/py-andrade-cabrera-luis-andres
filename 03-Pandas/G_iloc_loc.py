#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 08:04:51 2019

@author: andres
"""


import pandas as pd
path_save_full_bin = "/home/andres/Dropbox/6to&7moSemestre/IDW/py-andrade-cabrera-luis-andres/03-Pandas/data/artwork_data_full.pickle"
df = pd.read_pickle(path_save_full_bin)

primero = df.loc[0]

primero = df.iloc[0]

df2= df.set_index("id")
primero = df2.loc[0]

primero = df2.iloc[0]

datos = {
        "nota 1":{
                "pepito":7,
                "Alisson":8,
                "Valeria":9},
        "disciplina":{
                "pepito":5,
                "Alisson":9,
                "Valeria":2}
        }

notas = pd.DataFrame(datos)
notas.loc[0] # Se filtra con labels de los indices
notas.iloc[0] # Se filtra con los indices


