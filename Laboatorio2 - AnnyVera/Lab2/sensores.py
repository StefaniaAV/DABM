   
import csv
from tabulate import tabulate
import datetime

class Sensor:
    def __init__ (self, nombre):
        self.nombre = nombre
        
    def registrar_lecturas(self, paciente, fecha, hora, valor): #metodo
        self.paciente = paciente
        self.valor = []
        self.valor.append(valor)
        self.fecha = fecha
        self.hora = hora
        
        Registros = [self.paciente, self.hora, self.fecha, self.valor]
        with open("Registros.csv","w", newline = "") as file:
            writer = csv.writer(file, delimiter =";")
            writer.writerow(["Nombre paciente", "Hora", "Fecha", self.nombre])
            writer.writerows(Registros)
    
    
class Paciente:
    def __init__ (self, paciente, patologia, sensores):
        self.paciente = paciente
        self.patologia = patologia
        self.sensores = sensores
        
    def registar_lecturas(self, valores):
       for i, sensor in enumerate(self.sensores):
           sensor.registrar_lecturas(self.paciente,1,1,valores[i])            
        
    def reporte_lecturas():
        pass
    #toca leer el archivo csv toca guardarlo en algo y luego toca ponerlo en tabulate
        #keys = []
        #print(tabulate(matriz, keys, tablefmt="outline"))
    

sensor1 = Sensor("Sensor1")
sensor2 = Sensor("Sensor2")

P1 = Paciente("Paula","Espaticidad",[sensor1, sensor2])
print(P1.sensores[0].nombre)
print(P1.sensores[1].nombre)
