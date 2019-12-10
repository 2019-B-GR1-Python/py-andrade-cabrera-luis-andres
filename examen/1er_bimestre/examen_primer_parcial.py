#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 07:15:28 2019

@author: andres
"""

import numpy as np
import pandas as pd

#2) Crear un vector de ceros de tamaño 10
array_of_zeros = np.zeros(10)
#3) Crear un vector de ceros de tamaño 10 y el de la posicion 5 sea igual a 1
array_of_zeros_with_5 = np.zeros(10)
array_of_zeros_with_5[4] = 1
#4) Cambiar el orden de un vector de 50 elementos, el de la posicion 1 es el de la 50 etc.
array_of_fifty = np.arange(50)
reversed_array_of_fifty = array_of_fifty[::-1]
#5) Crear una matriz de 3 x 3 con valores del cero al 8
matrix_square_3 = np.arange(9)
matrix_square_3 = matrix_square_3.reshape(3,3)
#6) Encontrar los indices que no sean cero en un arreglo
array = np.array([1,2,0,0,4,0])
indice = 0
for value_not_0 in (array !=0):
    if value_not_0:
        print(indice)
    indice += 1

#7) Crear una matriz de identidad 3 x 3
identity_matrix = np.identity(3)
#8) Crear una matriz 3 x 3 x 3 con valores randomicos
matrix_cube_3 = np.random.randint(10, size=(3,3,3))
print(matrix_cube_3.shape)
#9) Crear una matriz 10 x 10 y encontrar el mayor y el menor
matrix_10 = np.random.randint(1000, size=(10,10))
max_val = matrix_10.max()
min_val = matrix_10.min()
#10) Sacar los colores RGB unicos en una imagen (cuales rgb existen ej: 0, 0, 0 - 255,255,255 -> 2 colores)

#11) ¿Como crear una serie de una lista, diccionario o arreglo?
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))
serie_from_list = pd.Series(mylist)
serie_from_array = pd.Series(myarr)
serie_from_dict = pd.Series(mydict)
#12) ¿Como convertir el indice de una serie en una columna de un DataFrame?
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))
ser = pd.Series(mydict) 
dataframe = pd.DataFrame(ser)
dataframe = dataframe.reset_index()
#13) ¿Como combinar varias series para hacer un DataFrame?
ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))
df_from_series = pd.DataFrame(ser1)
df_from_series[2] = ser2
#14) ¿Como obtener los items que esten en una serie A y no en una serie B?
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])
ser3 = pd.Series(list(set(ser1) & set(ser2)))
#15) ¿Como obtener los items que no son comunes en una serie A y serie B?
#16) ¿Como obtener el numero de veces que se repite un valor en una serie?
ser = pd.Series(np.take(list('abcdefgh'), np.random.randint(8, size=30)))
ser.value_counts() 

#17) ¿Como mantener los 2 valores mas repetidos de una serie, y a los demas valores cambiarles por 0 ?

#18) ¿Como transformar una serie de un arreglo de numpy a un DataFrame con un shape definido?

#19) ¿Obtener los valores de una serie conociendo la posicion por indice?
#20) ¿Como anadir series vertical u horizontalmente a un DataFrame?
ser1 = pd.Series(range(5))
ser2 = pd.Series(list('abcde'))

#21)¿Obtener la media de una serie agrupada por otra serie?
#22)¿Como importar solo columnas especificas de un archivo csv?
path = "BostonHousing.csv"
columnas = ["crim",'zn','indus','nox']
df = pd.read_csv(
        path,
        nrows = 10,
        usecols = columnas)