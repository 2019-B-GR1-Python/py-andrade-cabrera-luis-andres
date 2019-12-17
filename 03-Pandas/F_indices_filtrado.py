#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 07:49:54 2019

@author: andres
"""

import pandas as pd
path_save_full_bin = "/home/andres/Dropbox/6to&7moSemestre/IDW/py-andrade-cabrera-luis-andres/03-Pandas/data/artwork_data_full.pickle"
df = pd.read_pickle(path_save_full_bin)

serie_artistas_repetidos = df['artist']

artistas = pd.unique(serie_artistas_repetidos)

artistas.size
len(artistas)
# Determinar solamente las orbas de William, Blake
blake = df['artist'] == "Blake, William"
blake.value_counts()
df["artist"].value_counts()
# Filtrado de indices
df_blake = df[blake]