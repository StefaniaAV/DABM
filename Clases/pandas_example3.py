import pandas as pd
import os
cwd = os.getcwd()

'''

archivo = cwd +"/Clases/libs/vital_signs.csv"

vital_signs = pd.read_csv(archivo, index_col = 'timestamp', parse_dates = True) #parse_dates para lo que vea que tiene formacho de fecha lo convierta a formato de fecha
 
#Calcular la frecuencia promedio por hora

heart_rade = vital_signs['heart_rate'].resample('1H').mean() #muestree en rangos de 1H y sobre cada rango se le saca el promedio 
print(heart_rade)

'''

# Ejemplo 2

'''
archivo = cwd +"/Clases/libs/patient_data.csv"
patient_data = pd.read_csv(archivo)

archivo2 = cwd +"/Clases/libs/population_data.csv"
population_data = pd.read_csv(archivo2)

#fusion de datos
merge_data = pd.merge(patient_data, population_data, on = "Zip Code")  #on la llave con la que se va unir


merge_data['Chronic Condition %'] = merge_data['Chronic Condition Count']/merge_data['Population'] * 100 #columna nueva dividiendo las dos columnas de condicion cronica y population en 100
print(merge_data)

'''