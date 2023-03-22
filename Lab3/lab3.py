import serial 
import struct
import time
import csv

class SerialPort:
    def __init__(self, port, baudrate):
        self.serial_port = serial.Serial(port = port, baudrate = baudrate)
        
    def read_data(self):
        return self.serial_port.readline().decode().strip() #de byte a string)
    
    def write(self,valor):
        self.serial_port.write(valor)
        
def num_to_range(num, minimo, maximo):
    if num >= maximo:
        return 255
    return (255*(num-minimo)/(maximo-minimo)) if num >= minimo else 0

    
def main():
    arduino = SerialPort("COM5", 9600)

    with open("Rango.csv","w", newline = "") as file: 
        writer = csv.writer(file, delimiter =";")
        writer.writerow([3.65, 4.68])
        
    while (1):
        print("1. Para ingresar datos\n2. Cargar datos CSV")
        entrada = input()
            
        if entrada == "1":
            print("Ingrese el mínimo del rango")
            minimo = float(input())
            print("Ingrese el maximo del rango")  
            maximo = float(input())
            
            with open("Rango.csv","w", newline = "") as file: 
                writer = csv.writer(file, delimiter =";")
                writer.writerow([minimo, maximo])
            break

        elif entrada == "2":
            with open("Rango.csv","r", newline = "") as file:   
                reader = csv.reader(file, delimiter =";")
                rango = next(reader)
                minimo,maximo = float(rango[0]), float(rango[1])
            break #para salir de los loops
                
        else:
            print("El numero ingresado no es una opcion del menu, por favor intente nuevamente")
            
    
    while (True):
        data = float(arduino.read_data())
        valor = num_to_range(data, minimo, maximo)
        print(data, valor)
       # print(valor)
        arduino.write(struct.pack(">B",int(valor))) #convertir valor de string a binario
        
        time.sleep(0.1)
            
try: 
    main()
except KeyboardInterrupt:
    print("Programa terminado")