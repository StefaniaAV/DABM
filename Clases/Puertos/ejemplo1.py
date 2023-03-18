import serial

class SerialPort:
    def __init__(self, port, baudrate):
        self.serial_port = serial.Serial(port = port, baudrate = baudrate)
        
        
        
    def read_data(self):
        return self.serial_port.readline().decode().strip() #para limpiar el dato de la comunicación decode para pasarlo a binario serial strip (para caracter)
        
port = SerialPort("COM3", 9600)
while (True):
    data = port.read_data()
    print("Dato recibido:", data)
    
port.close()

#320 oscuro 28