#-----------------------------laboratorio 5 -------------------------
#creacion de una lista de diferentes tipos de variables
myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]

#con este ciclo for recorremos todos los elementos de la lista, debido a que ya trae indice 
#primero se muestra el valor contenido y despues el tipo de dato
for item in myMixedTypeList:
    print("{} is of the data type {}".format(item,type(item)))