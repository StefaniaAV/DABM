import csv 

update_records = []
with open('patient_records.csv','r') as file:
    reader = csv.reader(file, delimiter = ";")
    header = next(reader)
    nombre = input("Nombre del paciente que desea actualizar:")
    
    for row in reader: 
        while nombre not in row[0]:
            print("El nombre del paciente no se encuentra en la base de datos")
            nombre = input("Nombre del paciente que desea actualizar:")
        
        for row in reader:
            #para actualizar los datos de los pacientes
            if row[0] == nombre:
                row[1] == input("Ingerese genero:")
                row[2] == input("Ingrese edad:")
                row[3] == input("Ingrese Patología:")

            update_records.append(row)
        
    
with open('patient_records.csv','w', newline = "") as file:  #w para write el database
    writer = csv.writer(file, delimiter = ';')
    writer.writerow(header)
    writer.writerows(update_records)
    
    
    
#son archvios planos