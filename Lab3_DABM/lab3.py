import serial 
import struct
import time
import csv

class SerialPort:
    def __init__(self, port, baudrate):
        self.serial_port = serial.Serial(port = port, baudrate = baudrate) #Para crear un puerto serial 
        
    def read_data(self):
        return self.serial_port.readline().decode().strip() #Para decodificar a bytes
    
    def write(self,valor):
        self.serial_port.write(valor) #Para escribir en el puerto serial
        
def num_to_range(num, minimo, maximo): #Para los rangos de entrada 
    if num >= maximo:
        return 255 #Cuando el valor es maximo se prende totalmente
    return (255*(num-minimo)/(maximo-minimo)) if num >= minimo else 0 #Cuando el valor es menor al minimo se apaga toltalmente

    
def main():
    arduino = SerialPort("COM5", 9600) #Puerto del computador

    with open("Rango.csv","w", newline = "") as file:  #Para escribir un valor de refencia inicial
        writer = csv.writer(file, delimiter =";")
        writer.writerow([4.32, 4.91])
        #1.85, 4.23
        
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
        data = float(arduino.read_data()) #Para leer el valor del divisor de la fotoresistencia
        valor = num_to_range(data, minimo, maximo) 
        #print(data, valor)
       # print(valor)
        arduino.write(struct.pack(">B",int(valor))) #Convertir valor de entero a bytes y escribir en el puerto
        
        time.sleep(0.05)
            
try: 
    main()
except KeyboardInterrupt:
    print("Programa terminado")