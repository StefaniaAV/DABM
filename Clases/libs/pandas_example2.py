import pandas as pd
import matplotlib.pyplot as plt
import os

'''
cwd = os.getcwd()
archivo = cwd + "/Clases/libs/ecg_data.csv"
ecg_data = pd.read_csv(archivo)

time = ecg_data['time']
signal = ecg_data['signal']

plt.plot(time,signal)
plt.xlabel('Time (s)')
plt.ylabel('ECG signal (mv)')
plt.title('ECG signal Over Time')
plt.show()


x = [20, 25, 35, 40, 45, 50, 55, 60]
y = [80, 100, 125, 140, 160, 180, 200,220]

plt.scatter(x,y)
plt.title("Indice de masa corporal VS Azucar en sangre")
plt.xlabel('IMC (kg/m2)')
plt.ylabel('Azucar en sangre (md/Dl)')
plt.show()


#grafica tipo barras
labels = ["Cancer de seno", "Cancer de prostata", "Cancer de pulmon","Cancer de colon","otro"]
values = [30, 20, 15, 10, 25]

plt.bar(labels, values, color = ["lime", "pink", "yellow", "green", "magenta", "blue"])
plt.title("Frecuencia de tipo de Cáncer")
plt.xlabel("Tipo de Cáncer")
plt.ylabel("Porcentaje de pacientes (%)")

plt.show()


#mapas de calor

import numpy as np
data = np.random.rand(5,5)
print(data)

plt.imshow(data, cmap = 'coolwarm')

plt.title("correlación de genes")
plt.xlabel("Genes")
plt.ylabel("Genes")

plt.colorbar()
plt.show()


#diagrama de cajas
data = [20, 22, 25, 26, 26, 28, 30, 31, 33, 35, 40, 42, 45]

plt.boxplot(data)

plt.title("Distribución de indice de masa corporal")
plt.ylabel("IMC (kg/m2)")
plt.show()
'''

#diagrama de pastel

labels = ["Cirugia", "Radiacion","Quimioterapia","Otros"]
values = [50, 30, 15, 5]
plt.pie(values,labels = labels)
plt.title("Tipos de procedimientos medicos")

plt.show()