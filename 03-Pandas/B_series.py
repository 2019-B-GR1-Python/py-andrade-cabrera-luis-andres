import numpy as np
import pandas as pd

lista_numeros = [1,2,3,4]
tupla_numeros = (1,2,3,4)
np_numeros = np.array((1,2,3,4))


serie_a = pd.Series(lista_numeros)
serie_b = pd.Series(tupla_numeros)
serie_c = pd.Series(np_numeros)
serie_d = pd.Series([True,
        False,
        False,
        12,
        12.12,
        "Andrés",
        None,
        (),
        [],
        {"Nombre":"Andrés"}])

lista_ciudades = ["Ambato",
                "Cuenca",
                "Loja",
                "Quito"]
series_ciudad = pd.Series(
                lista_ciudades,
                index=[
                "A",
                "C",
                "L",
                "Q"
                ])
series_ciudad["Q"]
series_ciudad[3]

valores_ciudad = {
                "Ibarra":9500,
                "Guayaquil":10000,
                "Cuenca":7000,
                "Quito":8000,
                "Loja":3000
                }
serie_valor_ciudad = pd.Series(
                valores_ciudad
                )
serie_valor_ciudad[0]
serie_valor_ciudad["Ibarra"]

ciudades_menores_5000 = serie_valor_ciudad < 5000

s5 = serie_valor_ciudad[ciudades_menores_5000]

serie_valor_ciudad = serie_valor_ciudad * 1.1

serie_valor_ciudad["Quito"] -= 50

print("Lima" in serie_valor_ciudad)
print("Loja" in serie_valor_ciudad)

respuesta_square = np.square(serie_valor_ciudad)
