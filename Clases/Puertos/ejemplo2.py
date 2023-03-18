import serial

class SerialPort:
    def __init__(self, port, baudrate):
        self.serial_port = serial.Serial()
        self.port = port
        self.baudrate = baudrate
        
    def open(self):
        if not self.serial_port.is_open :
            self.serial_port.port= self.port    #Para mirar si no esta abierto
            self.serial_port.baudrate = self.baudrate
            self.serial_port.open()
            
    def is_open(self):
        return self.serial_port.is_open  #is open es de la libreria
        
    def close(self):
        if self.is_open():
            self.serial_port.close()    
    
    def read_data(self):
        return self.serial_port.readline().decode().strip()
    
port = SerialPort("COM5", 9600)
port.open()
if port.is_open():
    while (True):
        data = port.read_data()
        print("Dato recibido:", data)
        
port.close()