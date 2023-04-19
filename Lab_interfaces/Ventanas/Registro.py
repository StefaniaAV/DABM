import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel,QLineEdit, QPushButton
import csv
import os

class RegisterWindow(QWidget):
    def __init__(self, usuariorep, usuarioexito):
        super().__init__()
        self.urep = usuariorep
        self.login = None
        self.exito = usuarioexito
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle('Registrarse al sistema') #crear ventana
        self.setGeometry(100, 100, 300, 200) #tamaño de la ventana (donde quiero que empiece, ancho, largo)
        
        layout = QVBoxLayout() #ventana vertical 
        
        label_username = QLabel('Nuevo usuario:')
        layout.addWidget(label_username) #adicionar a la ventana
        
        self.edit_user_name = QLineEdit() #para escribir en el cuadro de texto 
        layout.addWidget(self.edit_user_name)
        
        label_password = QLabel('Nueva contraseña:')
        layout.addWidget(label_password)
        
        self.edit_password = QLineEdit()
        self.edit_password.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.edit_password)
        
        label_perfil = QLabel('Perfil:')
        layout.addWidget(label_perfil)
        
        self.edit_perfil = QLineEdit()
        layout.addWidget(self.edit_perfil)
        
        btn_registrar = QPushButton('Registrarme') #creacion de los botones
        btn_registrar.clicked.connect(self.auth)
        layout.addWidget(btn_registrar)
        
        btn_ingresar = QPushButton('Ingresar') #creacion de los botones
        btn_ingresar.clicked.connect(self.ing)
        layout.addWidget(btn_ingresar)
                
        self.setLayout(layout)
        
    def auth(self):
        
        self.username = self.edit_user_name.text()
        self.password = self.edit_password.text()
        self.perfil = self.edit_perfil.text()

        self.datos = [self.username, self.password, self.perfil]
        
        cwd = os.getcwd()
        archivo = cwd + "/Lab_interfaces/Archivos/usuarios.csv"
        with open(archivo,"r") as file:  #la r es solo para read
            reader = csv.reader(file, delimiter = ",")
            header = next(reader)
            #self.username = None
            for row in reader:
                if row[0] == self.username:
                    self.urep.show()
                    print("Repetido")
                    return
                        
            cwd = os.getcwd()
            archivo = cwd + "/Lab_interfaces/Archivos/usuarios.csv"
            print(self.datos)
            with open(archivo,"a", newline = "") as file: 
                writer = csv.writer(file, delimiter =",")
                writer.writerow(self.datos)
        self.exito.show()
                    
    def ing(self):
        #self.l.show()
        print("Ingresar")
        self.close()
        self.login.show()
       
        
    def registerlogin(self, loginwindow):
        self.login = loginwindow
        
        
        
    
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
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    stylesheet = load_stylesheet()
    app.setStyleSheet(stylesheet)
    
    Register_window = RegisterWindow()
    Register_window.show()
    
    sys.exit(app.exec()) #para controlar el cierre de la ventana