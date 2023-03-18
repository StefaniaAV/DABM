import pyfirmata
import serial
import time

puerto = serial.Serial("COM5", 9600) #Puerto COM de emulación en USB
pin = (13) #PIN donde va conectado el LED
data = []
 
#Conexión con placa Arduino
#print("Conectando con Arduino por USB...")
tarjeta = pyfirmata.Arduino(puerto)
#print("Conectado a Arduino por USB...")

a = 1

while a == 1:
    #value = puerto.readline().decode().strip()
    #data.append(value)
    #if data 
    #print("Encendiendo LED...")
    time.sleep(10)
    tarjeta.digital[pin].write(1)
    #print("Encendido LED...")
    time.sleep(10)
    #tarjeta.pass_time(3)
    #print("Apagando LED...")
    tarjeta.digital[pin].write(0)
    #print("Apagado LED...")
    time.sleep(10)
    #tarjeta.pass_time(3)
