import os
from Ventanas.Ingreso import LoginWindow, load_stylesheet
from Ventanas.Datos import MainWindow
from Ventanas.Accdenegado import Denegado
from Ventanas.Registro import RegisterWindow

from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap
 
import sys   


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    stylesheet = load_stylesheet()
    app.setStyleSheet(stylesheet)
    
    main_window = MainWindow()
    acceso_denegado = Denegado() #para el ejemplo toca crear la de acceso denegado recordar.
    
    
    register_window = RegisterWindow()
    
    login_window = LoginWindow(main_window, acceso_denegado, register_window)
    
    login_window.show()
       
    sys.exit(app.exec()) 