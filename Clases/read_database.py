import csv

with open("patient_records.csv","r") as file:
    #la r es solo para read
    reader = csv.reader(file, delimiter = ";")
    next(reader) #para que no salgan los encabezados
    for row in reader:
        #print(row)
        print("Nombre:", row[0])
        print("Genero:", row[1])
        print("Edad", row[2])
        print("Patologia", row[3])
        print("\n")