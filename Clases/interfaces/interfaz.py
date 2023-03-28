import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel,QLineEdit, QPushButton


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle('Ingreso ak sistema DABM') #crear ventana
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
        
        self.setLayout(layout)
        
    def auth(self):
        #print('Boton pulsado')
        username = self.edit_user_name.text()
        password = self.edit_password.text()
        
        if self.validate_credentials(username, password):
            print('Acceso concedido')
        else:
            print('Acceso denegado')
            
    def validate_credentials(self, username, password): 
        return username == "usuario" and password == "password" #en este caso se mira que el usuario sea igual a "usario" si no es igual es acceso denegado
        
        
def load_stylesheet():
    return """
        QWidget {
            background-color: LightGray;
            box-shadow: 5px 5px 5px #FFDAB9;
        }
        QLabel{
            font-size: 14px;
            color: MediumOrchid;
        }
        QLineEdit{ 
            background-color: LightBlue; 
            border: 1px solid DarkSlateBlue; 
            padding: 3px; 
            font-size: 14px; 
        } 
        QPushButton{ 
            background-color: LightCoral; 
            color: MediumVioletRed; 
            border: 1px solid Khaki; 
            padding: 5px; 
            font-size: 14px; 
        } 
        QPushButton:hover{ 
            background-color: Khaki; 
            border: 1px solid LightCoral; 
        }
    """
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    stylesheet = load_stylesheet()
    app.setStyleSheet(stylesheet)
    
    login_window = LoginWindow()
    login_window.show()
    
    sys.exit(app.exec()) #para controlar el cierre de la ventana