#---------------laboratorio 6 --------------------------------
#importe los módulos que utilizará:
import csv
import copy
#defina el diccionario que funcionará como tipo compuesto para leer los datos tabulares:
myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}
# Utilizará un bucle for para recorrer las claves y valores del diccionario.
for key, value in myVehicle.items():
    #se imprime la clave ; valor
    print("{} : {}".format(key,value))

#se crea la lista myInventorylist 
myInventoryList = []

#se abre el archivo car_feet.csv y se guarda dentro de la variable csvFile
with open('car_fleet.csv') as csvFile:
    #se lee el archviodonde su delimitadores es la coma , 
    csvReader = csv.reader(csvFile, delimiter=',')  
    #se creala varaiable linecounty se asigna el valor 0
    lineCount = 0 
    #se lee cada una de las lines, filas o regiones del archivo csvReader
    for row in csvReader:
        #si el valor de las lineas es 0
        if lineCount == 0:
            #se imprimie el nombre de la columna
            print(f'Column names are: {", ".join(row)}')
            # se aumenta en 1 el valor de linecount
            lineCount += 1  
        #si el valor de la linea linecount no es cero
        else:  
            #imprimie en cada una de las claves las posiscion que fueron separadas por , anteriormente
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  
            #se copia el valor de las variables dentro del diccionario myVehicle
            currentVehicle = copy.deepcopy(myVehicle)  
            currentVehicle["vin"] = row[0]  
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7] 
            #se agrega a la lista un vehiculo
            myInventoryList.append(currentVehicle)  
            lineCount += 1  
        #se imprime el nuemro total de lineas leidas en el documento
    print(f'Processed {lineCount} lines.')
    
    #se creaq un for para imprimi cada vehiculo de la lista
    for myCarProperties in myInventoryList:
        for key, value in myCarProperties.items():
            print("{} : {}".format(key,value))
            print("-----")