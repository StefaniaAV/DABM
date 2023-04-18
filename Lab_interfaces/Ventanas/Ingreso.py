import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel,QLineEdit, QPushButton
import csv
import os

class LoginWindow(QWidget):
    def __init__(self, datosWindow, accesodenegadoWindow, registerwindow):
        super().__init__()
        self.w = datosWindow
        self.accnegado = accesodenegadoWindow
        self.r = registerwindow
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle('Ingreso al sistema') #crear ventana
        self.setGeometry(100, 100, 300, 200) #tamaño de la ventana (donde quiero que empiece, ancho, largo)
        
        layout = QVBoxLayout() #ventana vertical 
        
        label_username = QLabel('Usuario:')
        layout.addWidget(label_username) #adicionar a la ventana
        
        self.edit_user_name = QLineEdit() #para escribir en el cuadro de texto 
        layout.addWidget(self.edit_user_name)
        
        label_password = QLabel('Contraseña:')
        layout.addWidget(label_password)
        
        self.edit_password = QLineEdit()
        self.edit_password.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.edit_password)
        
        btn_ingresar = QPushButton('Ingresar') #creacion de los botones
        btn_ingresar.clicked.connect(self.auth)
        layout.addWidget(btn_ingresar)
        
        btn_registrar = QPushButton('Registrarme') #creacion de los botones
        btn_registrar.clicked.connect(self.reg)
        layout.addWidget(btn_registrar)
        
        self.setLayout(layout)
        
    def reg(self):
        self.r.show()
        self.close()
        
    def auth(self):
        #print('Boton pulsado')
        username = self.edit_user_name.text()
        password = self.edit_password.text()
        
        if self.validate_credentials(username, password):
            print('Acceso concedido')
            self.w.show()
            self.close()
        else:
            self.accnegado.show()
            print('Acceso denegado')
            
    def validate_credentials(self, username, password): 
        cwd = os.getcwd()
        archivo = cwd + "/Lab_interfaces/Archivos/usuarios.csv"
        with open(archivo,"r") as file:  #la r es solo para read
                reader = csv.reader(file, delimiter = ",")
                header = next(reader)
                self.username = None
                for row in reader:
                    if row[0] == username:
                        self.username = row[0]
                        self.password = row[1]
                        
        if self.username is None: 
            return False 
                                      
        return username == self.username and password == self.password #en este caso se mira que el usuario sea igual a "usario" si no es igual es acceso denegado
        
        
def load_stylesheet():
    return """
        QWidget {
            background-color: GhostWhite;
        }
        QLabel{
            font-size: 15px;
            color: Black;
        }
        QLineEdit{ 
            background-color: Gainsboro; 
            border: 1px solid DarkSlateGrey; 
            padding: 3px; 
            font-size: 14px; 
            border-radius: 10;
            font: 75 8pt "Roboto Medium";
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
        
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
    
#     stylesheet = load_stylesheet()
#     app.setStyleSheet(stylesheet)
    
#     login_window = LoginWindow()
#     login_window.show()
    
#     sys.exit(app.exec()) #para controlar el cierre de la ventana