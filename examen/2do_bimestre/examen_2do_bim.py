import numpy as np
import pandas as pd
# 1) Crea un Dataframe de 10 registros y 6 columnas y consigue las 5 primeros y los 5 ultimos registros

arr_pand = np.random.randint(0,60,60).reshape(10,6)

dataframe_one = pd.DataFrame(arr_pand)
first_5 = dataframe_one.head(5)
last_5 = dataframe_one.tail(5)
# 2) Crear un dataframe pasando un arreglo de numpy de 6 x 4 con una fecha como indice y con columnas A, B, C, D randomico

arr_pand = np.random.randint(0,90,24).reshape(6,4)

dataframe_two = pd.DataFrame(arr_pand)
dataframe_two.columns = ["A","B","C","D"]
dataframe_two.index = pd.date_range(start='18/2/2020', periods=6)
# 4) Crear un Dataframe con 10 registros y 6 columnas y con una propiedad del Dataframe mostrar las columnas, con otro comando mostrar los valores.

arr_pand = np.random.randint(0,60,60).reshape(10,6)

dataframe_three = pd.DataFrame(arr_pand)
columns = list(dataframe_three.columns)
values = dataframe_three.values
# 5) Crear un Dataframe con 10 registros y 6 columnas y con una funcion del Dataframe describir estadisticamente el Dataframe

arr_pand = np.random.randint(0,60,60).reshape(10,6)

dataframe_four = pd.DataFrame(arr_pand)
description = dataframe_three.describe()

# 6) Crear un Dataframe con 10 registros y 6 columnas y con una funcion del Dataframe transponer los datos

arr_pand = np.random.randint(0,60,60).reshape(10,6)

dataframe_five = pd.DataFrame(arr_pand)

transpuesta = dataframe_five.transpose()
# 7) Crear un Dataframe con 10 registros y 6 columnas y Ordenar el dataframe 1 vez por cada columna, ascendente y descendente

arr_pand = np.random.randint(0,60,60).reshape(10,6)

dataframe_six = pd.DataFrame(arr_pand)
dataframe_six.columns = ["A","B","C","D","E","F"]
ordered_dataframe_zero = dataframe_six.sort_values(by=['A'])
ordered_dataframe_one = dataframe_six.sort_values(by=['B'])
ordered_dataframe_two = dataframe_six.sort_values(by=['C'])
ordered_dataframe_three = dataframe_six.sort_values(by=['D'])
ordered_dataframe_four = dataframe_six.sort_values(by=['E'])
ordered_dataframe_five = dataframe_six.sort_values(by=['F'])

ordered_descending_zero = dataframe_six.sort_values(by='A', ascending=False)
ordered_descending_one = dataframe_six.sort_values(by='B', ascending=False)
ordered_descending_two = dataframe_six.sort_values(by='C', ascending=False)
ordered_descending_three = dataframe_six.sort_values(by='D', ascending=False)
ordered_descending_four = dataframe_six.sort_values(by='E', ascending=False)
ordered_descending_five = dataframe_six.sort_values(by='F', ascending=False)

# 8) Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 y seleccionar en un nuevo Dataframe solo los valores mayores a 7

arr_pand = np.random.randint(1,11,60).reshape(10,6)

dataframe_seven = pd.DataFrame(arr_pand)

more_than_7_dataframe = dataframe_seven.where(dataframe_seven >7)

# 9) Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 o valores NaN. Luego llenar los valores NaN con 0.

arr_pand = np.random.randint(1,11,60).reshape(10,6)

dataframe_eight = pd.DataFrame(arr_pand)
dataframe_eight[0][2] = np.nan
dataframe_eight[1][3] = np.nan
dataframe_eight[2][4] = np.nan

dataframe_eight_filled = dataframe_eight.fillna(0)

# 10) Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 y sacar la media, la mediana, el promedio

arr_pand = np.random.randint(1,11,60).reshape(10,6)

dataframe_nine = pd.DataFrame(arr_pand)
dataframe_nine_media_promedio = dataframe_nine.mean()
dataframe_nine_mediana = dataframe_nine.median()

# 11) Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10, luego crear otro dateframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 y anadirlo al primer Dataframe

arr_pand = np.random.randint(1,11,60).reshape(10,6)

dataframe_ten = pd.DataFrame(arr_pand)

new_arr_pand = np.random.randint(1,11,60).reshape(10,6)

new_dataframe_ten = pd.DataFrame(new_arr_pand)

dataframe_ten_appended = dataframe_ten.append(new_dataframe_ten)

# 12) Crear un Dataframe con 10 registros y 6 columnas llenas de strings. Luego, unir la columna 1 y 2 en una sola, la 3 y 4, y la 5 y 6 concatenando su texto.
list_strings = ["Charisse  ","Archie  ","Yun  ","Krystle  ","Alexa  ","Natalya  ","Reyna  ","Delta  ","Carroll  ","Norman  ","Willian  ","Tad  ","Shalonda  ","Candis  ","Hortensia  ","Chloe  ","Barbra  ","Michelle  ","Alyce  ","Harriette  ","Danille  ","Lakeesha  ","Megan  ","Frederica  ","Kristy  ","Adah  ","Senaida  ","Kacy  ","Trula  ","Annabel  ","Ayanna  ","Jacob  ","Lakia  ","Britni  ","April  ","Mireille  ","Donna  ","Jodee  ","Jeanetta  ","Daina  ","Shana  ","Elene  ","Henry  ","Priscila  ","Celinda  ","Louann  ","Deloris  ","Sandra  ","Marget  ","Jonelle  ","Brad  ","Julee  ","Dori  ","Jasper  ","Claudie  ","Mayme  ","Gena  ","Dalton  ","Lue  ","Luke"]
arr_pand = np.array(list_strings).reshape(10,6)
dataframe_eleven = pd.DataFrame(arr_pand)
dataframe_eleven_concat = pd.DataFrame()
dataframe_eleven_concat["1+2"] = dataframe_eleven[0] + dataframe_eleven[1]
dataframe_eleven_concat["3+4"] = dataframe_eleven[2] + dataframe_eleven[3]
dataframe_eleven_concat["5+6"] = dataframe_eleven[4] + dataframe_eleven[5]


# 13) Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 enteros, obtener la frecuencia de repeticion de los numeros enteros en cada columna

arr_pand = np.random.randint(1,11,60).reshape(10,6)

dataframe_twelve = pd.DataFrame(arr_pand)
fq_colum_zero = dataframe_twelve[0].value_counts()
fq_colum_one = dataframe_twelve[1].value_counts()
fq_colum_two = dataframe_twelve[2].value_counts()
fq_colum_three = dataframe_twelve[3].value_counts()
fq_colum_four = dataframe_twelve[4].value_counts()
fq_colum_five = dataframe_twelve[5].value_counts()


# 14) Crear un Dataframe con 10 registros y 3 columnas, A B C, llenas de números randomicos del 1 al 10 enteros. Crear una nueva columna con el calculo por fila (A * B ) / C

arr_pand = np.random.randint(1,11,30).reshape(10,3)

dataframe_thirteen = pd.DataFrame(arr_pand)
dataframe_thirteen.columns = ["A","B","C"]

dataframe_thirteen["(A*B)/C"] = (dataframe_thirteen["A"] * dataframe_thirteen["B"])/ dataframe_thirteen["C"]
