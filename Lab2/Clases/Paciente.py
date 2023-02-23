import csv
from tabulate import tabulate

class Paciente:
    def __init__ (self, paciente, patologia, sensores):
        self.paciente = paciente
        self.patologia = patologia
        self.sensores = sensores
        
    def registar_lecturas(self, valores):
       for i, sensor in enumerate(self.sensores):  #enumerate me permite devolver el indice del objeto
           sensor.registrar_lecturas(self.paciente,self.patologia,valores[i])            
        
    def reporte_lecturas(self):
        for sensor in self.sensores:
            registro = self.paciente + "_" + self.patologia + ".csv"
            Matriz = []
            with open(registro,"r") as file:  #la r es solo para read
                reader = csv.reader(file, delimiter = ";")
                #next(reader) #para que no salgan los encabezados
               
                Matriz = [ row for row in reader]
        
        keys = ["Sensor", "Hora", "Fecha", "Valor"]
        print(tabulate(Matriz, keys, tablefmt="outline"))

        