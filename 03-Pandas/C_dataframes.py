#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 07:42:22 2019

@author: andres
"""

import numpy as np
import pandas as pd

arr_pand = np.random.randint(0,10,6).reshape(2,3)

dataframe_one = pd.DataFrame(arr_pand)
# Un dataframe es un conjunto de series
select_colum_zero = dataframe_one[0]
select_colum_one = dataframe_one[1]
select_colum_two = dataframe_one[2]

select_colum_zero[0]

new_colum_for_df = pd.Series([5,7])
# Simplest way to append a co
dataframe_one[3] = new_colum_for_df

dataframe_one[4] = select_colum_zero * select_colum_one

datos_fisicos = pd.DataFrame(
        arr_pand, 
        columns = [
                'Estatura (cm)',
                'Peso (kg)',
                'Edad (anios)'],
        index=['Adrian', 'Vicente'])

dataframe_one.index=["Andres","Vicente"]
dataframe_one.index=["vicente","Andres"]
dataframe_one.columns = ["A","B","C","D","F"]

