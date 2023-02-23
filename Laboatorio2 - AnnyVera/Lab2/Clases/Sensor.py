import csv
from datetime import datetime

class Sensor:
    def __init__ (self, nombre):
        self.nombre = nombre
        
    def registrar_lecturas(self, paciente, patologia, valor): #metodo
        self.paciente = paciente
        self.patologia = patologia
        self.valor = valor
        
        hora = datetime.now().time()
        fecha = datetime.now().date()
        
        registro = self.paciente + "_" + self.patologia + ".csv"
        Registros = [self.nombre, hora, fecha, self.valor]
        with open(registro,"a", newline = "") as file:   #me permite re escribir en el archivo sin truncarlo
            writer = csv.writer(file, delimiter =";")
            #writer.writerow(["Nombre paciente", "Hora", "Fecha", "Valor"])
            writer.writerow(Registros)
    