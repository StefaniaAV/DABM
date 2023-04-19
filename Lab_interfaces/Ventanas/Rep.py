import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel,QLineEdit, QPushButton

class Repetido(QWidget):
    def __init__ (self):
        super().__init__()
        
        layout = QVBoxLayout()
        self.setWindowTitle("Error")
        self.setGeometry(120, 120, 100, 100)
        
        label_combo = QLabel("El usuario registrado ya se encuentra en la base de datos, por favor ingrese otro diferente", self)
        label_combo.setGeometry(20, 10, 500, 20)
        layout.addWidget(label_combo)
        
        btn_ingresar = QPushButton('Ok') #creacion de los botones
        btn_ingresar.clicked.connect(self.auth)
        btn_ingresar.setGeometry(10, 420, 100, 20)
        layout.addWidget(btn_ingresar)
        
        self.setLayout(layout)
    
    def auth(self):
        self.close()
        
def load_stylesheets():
    return """
        QWidget{
            background-color: GhostWhite;
        }
        QLabel{
            font-size: 14px;
            color: Black;
            font: 10 10pt "Roboto Medium";
        }

        QPushButton{ 
            background-color: FireBrick; 
            color: White; 
            border: 1px solid AntiqueWhite; 
            padding: 6px; 
            font-size: 14px; 
            border-radius: 10;
            font: 10 10pt "Roboto Medium";
        } 
    """
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    stylesheets = load_stylesheets()
    app.setStyleSheet(stylesheets)
    
    main_window = Repetido()
    main_window.show()
    
    sys.exit(app.exec()) 