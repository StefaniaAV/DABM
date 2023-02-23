#archivos planos la informacion esta expuesta, se pueden borrar facilmente
#mientras que con los RDBMS las bases de datos se trabajan mediante instrucciones SQL (almacenamamiento)

import csv 

patient_records = [["Juan Perez", "Hombre", 30, "Enfermedad cardiaca"],["Lina Alvarez","Mujer", 25, "Asma"] , ["Pedro Ramirez", "Hombre", 40 ,"Diabetes"]]

with open("patient_records.csv","w", newline = "") as file:
    writer = csv.writer(file, delimiter =";") #elemento que describe el archvio
    writer.writerow(["Nombre", "Genero", "Edad", "Patologia"])#Para el encabezado
    writer.writerows(patient_records)
    
