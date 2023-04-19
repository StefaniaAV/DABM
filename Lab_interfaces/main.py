import os
from Ventanas.Ingreso import LoginWindow, load_stylesheet
from Ventanas.Datos import MainWindow
from Ventanas.Accdenegado import Denegado
from Ventanas.Registro import RegisterWindow
from Ventanas.Rep import Repetido
from Ventanas.confirmacion import Conf

from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap
 
import sys   


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    stylesheet = load_stylesheet()
    app.setStyleSheet(stylesheet)
    
    confirmacion_window = Conf()
    main_window = MainWindow()
    acceso_denegado = Denegado() #para el ejemplo toca crear la de acceso denegado recordar.
    
    #login2 = LoginWindow()
    usuario_repetido = Repetido()
    register_window = RegisterWindow(usuario_repetido, confirmacion_window)

    #register_window = RegisterWindow(login2(main_window, acceso_denegado, register_window))
    
    login_window = LoginWindow(main_window, acceso_denegado, register_window)
    register_window.registerlogin(login_window)
    login_window.show()
       
    sys.exit(app.exec())