import pandas as pd
import os

cwd = os.getcwd()
archivo = cwd + "/Clases/libs/medical_data.csv"
data = pd.read_csv(archivo)
print(data)
# print(data.columns)
# print(data['age'])
# print(data.describe())
# print(data.head())
# print(data.tail())

# clean_data = data.dropna()   #cuando los archivos me salen dañados
# print(clean_data)
# average_age = clean_data['age'].mean()

# print("Edad promedio:", average_age)


#desviacion estandar de un conjunto de datos que tan distantes son los datos de al media