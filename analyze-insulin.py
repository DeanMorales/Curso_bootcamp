#se usa la libreria RE para trabajar con expresiones reguales
import re

#abrimos el archivo de texto preproinsulin-seq
#utilizamos el comando with open
with open("preproinsulin-seq.txt", "r") as f:

    #leemos todo el contenido del archivo    
    raw_data = f.read()
#eliminar la palabra ORIGIN 
clean_data = re.sub(r"\bORIGIN\b", "",raw_data, flags=re.IGNORECASE)

#Eliminar el terminador de registro //
clean_data = clean_data.replace("//", "")
#eliminar cualquier cosa que no sea letra
clean_data = re.sub(r"[^A-Za-z]", "", clean_data)

#convertimos todo a minusculas
clean_data = clean_data.lower()

#abrir nuevamente el archivo prepoinsulin
with open("preproinsulin-seq.txt", "r") as f:
    #limpiamos el archivo 
    f.write(clean_data)

#calculamos_la longitud de prepoinsulina 
print("longitud prepoinsulin = ", len(clean_data))
#si la secuencia no teien e110 caracteres nos salimos del programa
if len(clean_data) !=110:
    print("error, la secuencia no teien 110 carateres")
    
#extraemos lis primeros 24 caracteres
lsinsulin = clean_data[0:25]

#etraemos del caracter 25 al 54
binsulin = clean_data[24:54]

#extraemos del caracater 55 al 89
cinsulin = clean_data[54:89]

#extraemos del caracter 90 al 110
ainsulin = clean_data[89-110]

#creamos los diferentes archivos
with open("lsinsulin-seq-clean.txt", "w") as f :
    f.write(lsinsulin)
    
with open("binsulin-seq-clean.txt", "w") as f :
    f.write(binsulin)
    
with open("cinsulin-seq-clean.txt", "w") as f :
    f.write(cinsulin)
    
with open("ainsulin-seq-clean.txt", "w") as f :
    f.write(ainsulin)

#verificamos el tamano de caracarteres
print("lsinsulin = ", len(lsinsulin))
#verificamos el tamano de caracarteres
print("binsulin = ", len(binsulin))
#verificamos el tamano de caracarteres
print("cinsulin = ", len(cinsulin))
#verificamos el tamano de caracarteres
print("ainsulin = ", len(ainsulin))

insulin = binsulin + ainsulin
#total de insulina
print("insulina procesada =  ", len(insulin))
#secuencia de la insulina
print("secuencia de la insulina= ", insulin)
