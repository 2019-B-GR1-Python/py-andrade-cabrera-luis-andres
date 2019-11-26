#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 08:20:48 2019

@author: andres
"""

import pandas as pd
import os

# 1) JSON CSV HTML XML ...
# 2) Binary files ->
# 3) Relational Databases

path = "data/artwork_data.csv"
df = pd.read_csv(
        path,
        nrows = 10)

columnas = ["id",'artist','title','medium','year',
            'acquisitionYear','height','width','units']
df2 = pd.read_csv(
        path,
        nrows = 10,
        usecols = columnas)

df3 = pd.read_csv(
        path,
        nrows = 10,
        usecols = columnas,
        index_col = 'id')

path_save = "data/artwork_data.pickle"

df3.to_pickle(path_save)
path_save_full_bin = "data/artwork_data_full.pickle"
df4 = pd.read_csv(
        path)
df4.to_pickle(path_save_full_bin)

df5 = pd.read_pickle(path_save_full_bin)
