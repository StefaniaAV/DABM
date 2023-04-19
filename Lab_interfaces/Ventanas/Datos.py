import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
import serial 
import time
import struct

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

class MainWindow(QWidget):
    def __init__ (self): #para herencia
        
        super().__init__()
        self.arduino = SerialPort("COM3", 9600)
        layout = QVBoxLayout()
        
        #self.setLayout(layout)
        
        self.setWindowTitle("Brillo y velocidad de un sensor")
        self.setGeometry(600,600, 500, 500)
        
        label_combo = QLabel("Escoger rangos máximos y mínimos para intensidad del LED", self)
        label_combo.setGeometry(20, 10, 500, 20)
        layout.addWidget(label_combo)
        
        #insertar una imagen
        label_image = QLabel(self)
        label_image.setGeometry(25, 50, 300, 155)
        pixmap = QPixmap("Lab_interfaces\Ventanas\Led.png")
        
        
        label_image.setPixmap(pixmap)
        layout.addWidget(label_image)
        
        label_combo = QLabel("Valor máximo", self)
        label_combo.setGeometry(25, 290, 110, 20)
        layout.addWidget(label_combo)
        self.sld = QSlider(Qt.Orientation.Horizontal, self)
        self.sld.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.sld.setGeometry(20, 320, 100, 20)  #(margen, posicion en y, largo del deslizador, tamaño)
        self.sld.valueChanged[int].connect(self.update)
        self.sld.setRange(0, 100)
        self.sld.setSingleStep(1)
        
        self.result_label = QLabel('', self)
        self.result_label.setGeometry(140, 320, 100, 20)

        layout.addWidget(self.sld)
        layout.addWidget(self.result_label)
  
        
        label_combo = QLabel("Valor mínimo", self)
        label_combo.setGeometry(25, 360, 110, 20)
        layout.addWidget(label_combo)
        self.sld2 = QSlider(Qt.Orientation.Horizontal, self)
        self.sld2.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.sld2.setGeometry(20, 380, 100, 20)  #(margen, posicion en y, largo del deslizador, tamaño)
        self.sld2.valueChanged[int].connect(self.update2)
        self.sld2.setRange(0, 100)
        self.sld2.setSingleStep(1)
        
        self.result_label2 = QLabel('', self)
        self.result_label2.setGeometry(140, 380, 100, 20)

        layout.addWidget(self.sld2)
        layout.addWidget(self.result_label2)
    
        #self.edit_valor = QLineEdit()
        #self.edit_valor.setGeometry(140, 380, 100, 20)
        #layout.addWidget(self.edit_valor)
        

    
        btn_ingresar = QPushButton('Ingresar') #creacion de los botones
        btn_ingresar.clicked.connect(self.auth)
        btn_ingresar.setGeometry(10, 420, 100, 20)
        layout.addWidget(btn_ingresar)
        
        self.setLayout(layout)
        
        
    def update(self, value):
        self.result_label.setText(f'{value * 5 / 100}')
        
    def update2(self, value):
        self.result_label2.setText(f'{value * 5 / 100}')
        
    def auth(self):
        maximo = self.sld.value()* 5 / 100
        
        minimo = self.sld2.value()* 5 / 100
        print(maximo, minimo)
        while (True):
            data = float(self.arduino.read_data()) #Para leer el valor del divisor de la fotoresistencia
            #self.edit_valor.setText("hola")
            #self.edit_valor.update()
            valor = num_to_range(data, minimo, maximo) 
            print(valor)
            #print(data, valor)
            # print(valor)
            self.arduino.write(struct.pack(">B",int(valor))) #Convertir valor de entero a bytes y escribir en el puerto
            
            time.sleep(0.05)
            
        
        
        
        
def load_stylesheets():
    return """
        QWidget{
            background-color: FloralWhite;
        }
        QLabel{
            font-size: 14px;
            color: Black;
            font: 10 10pt "Roboto Medium";
        }

        QPushButton{ 
            background-color: Tan; 
            color: Black; 
            border: 1px solid AntiqueWhite; 
            padding: 6px; 
            font-size: 14px; 
            border-radius: 10;
            font: 10 10pt "Roboto Medium";
        } 
        QPushButton:hover{ 
            background-color: AntiqueWhite; 
            border: 1px solid LightCoral; 
        }
    """
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    stylesheets = load_stylesheets()
    app.setStyleSheet(stylesheets)
    
    main_window = MainWindow()
    main_window.show()
    
    sys.exit(app.exec()) 