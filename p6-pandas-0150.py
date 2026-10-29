import numpy as np
import pandas as pd

serie_amigos=["Iris","Daniel","Farfan","Jazmin","Anais","Diego","Darrel"]
print(" --- Serie listado de amigos --- NC= 0150")
amigos=pd.Series(serie_amigos)
print(amigos)
serie_billetas=[20,50,100,200,500,1000]
print(" --- Serie listado de billeteas MX --- NC= 0150")
amigos=pd.Series(serie_billetas)
print(amigos)

#Diccionario Dataframe
serie_billetas=[20,50,100,200,500,1000]
serie_bletras=["veinte","cincuenta","cien","docientos","quinientos","mil"]
print(" --- Serie listado nombre y valor de billetas MX --- NC= 0150")
tablabilletes=pd.Series(serie_bletras, serie_billetas)
print(tablabilletes)

#Diccionario de valor de monedas y nombre
print("Datos de diccionario a DataFrame en pandas")
dic_monedas={
    "serie billetes": [20,50,100,200,500,1000],
    "serie bletras": ["veinte","cincuenta","cien","docientos","quinientos","mil"]
}

tablabilletes=pd.DataFrame(dic_monedas, index=["A","B","C","D","E","F"])
print(tablabilletes)

print("Casa de cambio de Zavala Medina NC= 0150")
