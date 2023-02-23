import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
import os


cwd = os.getcwd()
archivo = cwd + "/Clases/libs/ecg_data.csv"
ecg_data = pd.read_csv(archivo)

time = ecg_data['time']
signal = ecg_data['signal']

descripcion = ecg_data['signal'].describe() #descripcion de variables estadisticos de uuna columna en especifico
print(descripcion)

promedio = np.mean(ecg_data.signal)
print(promedio)

#tomar primeros 50 datos

# print(ecg_data['signal'].head (50)) #la propiedad head me definie cuantos datos quiero tomar de los primeros
# print(ecg_data['signal'].tail(50)) #la propiedad tail me define cuantos datos quiero tomar de los ultimos datos

promedio_dinamico = pd.DataFrame.rolling(ecg_data.signal, window = (100)).mean() #window es para al freuneica de muestreo
#print(promedio_dinamico)

promedio_dinamico = [promedio if math.isnan(x) else (x) for x in promedio_dinamico]

porcen = (20*promedio)/100

#print(promedio_dinamico)


ecg_data['promedio_dinamico'] = promedio_dinamico + porcen

# points = []
# time2 = []
# for i in range (len(signal)):
#     if ecg_data.promedio_dinamico[i] < signal[i]:
#         if signal[i+1] <= signal[i] and signal[i-1] < signal[i] :
#             points.append(signal[i])
#             time2.append(i+1)     
        
# print(points)    

#otra forma de detetcar puntos
cont = 0
rango = []
maximosx = []
maximosy = []
for punto in ecg_data.signal:
    if (punto <= ecg_data.promedio_dinamico[cont]) and (len(rango) < 1):
        cont += 1
    elif punto > ecg_data.promedio_dinamico[cont]:
        rango.append(punto)
        cont += 1
    else:
        maximo = max(rango)
        maximosy.append(maximo)
        maximox = cont - len(rango) + rango.index(maximo)
        maximosx.append(maximox + 1)
        
        rango = []
        cont += 1
        
#para calcular la frecuencia cardiaca
#frecuenica de muestreo 100 milisegundos
cont = 0
dist = []
while cont < len(maximosx) - 1:
    distancia = maximosx[cont + 1] - maximosx[cont]
    distancia = distancia / 100
    dist.append(distancia)
  
bpm = 60 / np.mean(dist)
print(bpm, round(bpm,1))


plt.plot(time,signal)
plt.plot(ecg_data.promedio_dinamico, color = 'r')

#plt.scatter(time2, points, color = 'black')
plt.scatter(maximosx, maximosy, color = 'orange')
plt.xlabel('Time (s)')
plt.ylabel('ECG signal (mv)')
plt.title('ECG signal Over Time')
plt.legend(loc = 4, framealpha = 0.6)
plt.show()


#para encotnrar al frecuencia cardiaca se toma la distancia de los puntos y se dividen
#para encontrar los puntos se calcula el valor promedio de todos los puntos y los valores que sean mayor al promedio que son los que me interesan