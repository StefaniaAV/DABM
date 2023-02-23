import os
import time
from Clases.Paciente import Paciente     #para usar la clase paciente en el main
from Clases.Sensor import Sensor    
import sys    


print("Este programa registra los datos tomados de sensores de un paciente con su hora, fecha y valor correspondiente. \nPara ello primero hay que registrar un paciente. Ingresar la información del paciente como: Nombre y Patologia")
while 1:
    sensores = []
    valores = []
    pacientes = []
    print("Ingrese el nombre del paciente")
    paciente = input()
    print("Ingrese la patologia del paciente")
    patologia = input()
    print("Ingrese el nombre del sensor del paciente")
    nombre = input()
    sensores.append(Sensor(nombre))
    print("¿Desea ingresar otro sensor? Ingrese si o no")
    boton = input().lower()
    while boton != "si" and boton != "no":
        print("El valor ingresado no corresponde a ninguna de las dos opciones")
        print("¿Desea ingresar otro sensor? Ingrese si o no")
        boton = input().lower()
    
    while boton == "si":
        print("Ingrese el nombre del sensor del paciente")
        nombre = input()
        sensores.append(Sensor(nombre))
        print("¿Desea ingresar otro sensor? escriba si o no")
        boton = input().lower()
        
        while boton != "si" and boton != "no":
            print("El valor ingresado no corresponde a ninguna de las dos opciones")
            print("¿Desea ingresar otro sensor? escriba si o no")
            boton = input().lower()
        
    p = Paciente(paciente, patologia, sensores)
    for i in sensores:
        print("Ingrese el valor del sensor " + i.nombre)
        valor = input()
        valores.append(valor)
    p.registar_lecturas(valores)
                
    print("Si desea ver los datos ingresados ingrese 1, si desea agregar otro paciente ingrese 2, para terminar el programa marque x.")
    boton2 = input().lower()
    while boton2 != "1" and boton2 != "2" and boton2 != "x":
        print("El valor ingresado no corresponde a ninguna de las dos opciones")
        print("Si desea ver los datos ingresados ingrese 1, si desea agregar otro paciente ingrese 2")
        boton2 = input()
    if boton2 == "x":
        print("Programa terminado")
        sys.exit()
    while boton2 == "1":
        p.reporte_lecturas()
        boton2 = "0"
    print("Si desea regsitrar otro paciente ingrese 1, para terminar el programa marque x")
    boton = input().lower()
    if boton == "x":
        print("Programa terminado")
        sys.exit()

    