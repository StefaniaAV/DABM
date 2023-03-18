import serial
import struct
import time

arduino = serial.Serial("COM3", 9600)

while True:
    data = int(input("Introduce valor (0-100):"))
    print("Brillo:", data, "%")
    #valor = 255*data/100 #porque arduino no recibe valores de 0 y 1 entonces se debe hacer una regla de 3 porque recibe valores hasta 255
    valor = int(255*data/100)
    arduino.write(struct.pack(">B",valor))
    time.sleep(0.5) #eliminar latencias en la comunicacion o ruido
    #arduino.write(str(valor).encode())