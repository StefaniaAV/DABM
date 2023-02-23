from datetime import datetime

hora_actual = datetime.now().date()

print(hora_actual)



def ejemplo_archivo():
    cwd = os.getcwd()
    ruta = cwd + "/lab2/archivos"
    nombre = "Juan"
    ruta = ruta + "/" + nombre + ".csv"
    
    patient_records = [["Juan Perez", "Hombre", 30, "Enfermedad cardiaca"],["Lina Alvarez","Mujer", 25, "Asma"] , ["Pedro Ramirez", "Hombre", 40 ,"Diabetes"]]

    with open(ruta,"w", newline = "") as file:
        writer = csv.writer(file, delimiter =";") #elemento que describe el archvio
        writer.writerow(["Nombre", "Genero", "Edad", "Patologia"])#Para el encabezado
        writer.writerows(patient_records)

#esto me da la direccion de mi director dentro de las carpetas de visual no directamente desde el computador 
#guardar los archivos sin improtar la ruta

#ejemplo_archivo()

p1 = Paciente("Pedro", "Fiebre", ["sensor1", "Sensor2"])
print(p1.paciente)

