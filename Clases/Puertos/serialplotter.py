import serial
import matplotlib.pyplot as plt
from drawnow import drawnow 

#config de puerto serial
ser = serial.Serial("COM5", 9600)

#inicializar la grafica
plt.ion()
fig = plt.figure()

paused = False

data = []

def update_graph():
    plt.title("Real time serial plotter")
    plt.ylabel("Voltaje")
    plt.ylim(0,30)
    plt.plot(data,'ro-') #:ks para que sean cuadrados negros
    
def pausar(event):
    global paused
    if event.dblclick:
        paused = not paused
        
x = fig.canvas.mpl_connect('button_press_event', pausar)

#bluce principal y representacion de los datos
while True:
    value = ser.readline().decode().strip()
    data.append(value)
    
    #cuantos datos queremos ver limitar la lista a un numero maximo de puntos 
    if len(data) > 50:
        data.pop(0)
        
    #actualizar grafica
    if not paused:
        drawnow(update_graph)
        
    

