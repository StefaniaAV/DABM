#prender y apagar un led
import serial

arduino = serial.Serial("COM3", 9600)

while True:
    data = input("Introduce ON/OFF/Salir:")
    if data == "ON":
        data = "H"
    if data == "OFF":
        data = "L"
    if data == "Salir":
        break
    else:
        arduino.write(data.encode()) #encode par mandarlo a lenguaje de arduino
        