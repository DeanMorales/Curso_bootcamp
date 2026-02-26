#declaramos una lista de nombre myFruitList e ingresamos 3 frutas utilizando ""
myFruitList = ["apple", "banana", "cherry"]
#imprimimos en consola la lista
print(myFruitList)
#imprimios el typo de variable que es myFrmyFruitList
print(type(myFruitList))
#se imprime cada uno de los elementos utilizando llaves cuadradas[] y dentro el indice de la lista 
print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])
#cambiamos el valor del indice 2 de la lista por "orange"
myFruitList[2] = "orange"
#imprimimos la lista con el cambio 
print(myFruitList)
# para crear la tupla se utilizan parentesis como si fuera una funcion
myFinalAnswerTuple= ("apple", "banana", "pineapple")
#impresion de la tupla 
print(myFinalAnswerTuple)
#imprimimos el tipo de dato que es la tupla 
print(type(myFinalAnswerTuple))
#imprimimos el primer valor de la tupla que es apple
print(myFinalAnswerTuple[0])
#imprimimos el segundo valor de la tupla que es banana
print(myFinalAnswerTuple[1])
#el tercer valor de la tupla qyue es pineapple
print(myFinalAnswerTuple[2])

#creacion del diccionario, se defini como una coleccion de palabras y conceptos
#no contienen indices numericos, mas bien se identifican por el nombrellamada CLAVE
myFavoriteFruitDictionary = {
    #formato  "Clave" : "Valor, se respeta los corchetes dos puntos y comas al final
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}
#imprimimos el contenido del diccionario
print(myFavoriteFruitDictionary)
#imprimimos el tipo de variable del diccionario
print(type(myFavoriteFruitDictionary))
#accedemos a cada valor del diccionario
#accedemos al valor de akua que es apple 
print(myFavoriteFruitDictionary["Akua"])
#imprimimos el valor de saanvi que es banana
print(myFavoriteFruitDictionary["Saanvi"])
#imprimimos el valor de paulo que es pineapple
print(myFavoriteFruitDictionary["Paulo"])