import serial 
import struct
import time
import csv

class SerialPort:
    def __init__(self, port, baudrate):
        self.serial_port = serial.Serial(port = port, baudrate = baudrate)
        
    def read_data(self):
        return self.serial_port.readline().decode().strip() #de byte a string
    
    def write(self,valor):
        self.serial_port.write(valor)
        
def num_to_range(num, inMin, inMax, outMin, outMax):
  return outMin + (float(num - inMin) / float(inMax - inMin) * (outMax- outMin))
    
def main():
    arduino = SerialPort("COM5", 9600)

    with open("Rango.csv","w", newline = "") as file: 
        writer = csv.writer(file, delimiter =";")
        writer.writerow([0, 255])
        
    while (1):
        print("1. Para ingresar datos\n2. Cargar datos CSV")
        entrada = input()
            
        if entrada == "1":
            print("Ingrese el mínimo del rango")
            minimo = int(input())
            while not (0 <= minimo <= 255):
                print("El valor ingresado no esta dentro del rango permitido 0 255 ",minimo)
                print("Ingrese el mínimo del rango")
                minimo = int(input())
                
            print("Ingrese el máximo del rango")
            maximo = int(input())
            
            while not (0 <= maximo <= 255) or maximo <= minimo:
                if not (0 <= maximo <= 255):
                    print("El valor ingresado no esta dentro del rango permitido 0 255")
                    
                else:    
                    print("El maximo: ", maximo, "es menor que el minimo: ",minimo)
                print("Ingrese el máximo del rango")
                maximo = int(input())     
            
            with open("Rango.csv","w", newline = "") as file: 
                writer = csv.writer(file, delimiter =";")
                writer.writerow([minimo, maximo])
            break

        elif entrada == "2":
            with open("Rango.csv","r", newline = "") as file:   
                reader = csv.reader(file, delimiter =";")
                rango = next(reader)
                minimo,maximo = int(rango[0]), int(rango[1])
            break #para salir de los loops
                
        else:
            print("El numero ingresado no es una opcion del menu, por favor intente nuevamente")
            
    while (True):
        data = float(arduino.read_data())
        valor = int(255*data/5)
        valor = num_to_range(valor, 0, 255, minimo, maximo)
        arduino.write(struct.pack(">B",int(valor))) #convertir valor de string a binario
        print(valor)
        time.sleep(0.5)
            
try: 
    main()
except KeyboardInterrupt:
    print("Programa terminado")