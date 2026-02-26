#creamos una variable my_string y en ella guardamos el texto this is a string
myString="this is a string"
#imprimimos
print(myString)
#imprimimos el tipo de datos
print(type(myString))
#imprimimos my variable y el tipo de dato que es en consola
print(myString + " is of the data type " + str(type(myString)))
#Creamos variable firsstring y dentro el dato Water
firstString = "water"
#declaramos la segunda variable y le asignamos el valor fall
secondString = "fall"
#creamos una 3ra variable donde concatenamos first y second string 
thirdString = firstString + secondString
#imprimimos el valor de thirdstring
print(thirdString)
#con la funcion input llamamos ingreso de usuario por consola
name=input("cual es tu nombre ?: ")
print("tu nombre es: "+name)
#declaramos color y metemos el valor desde la consola con input
color = input("What is your favorite color?  ")
#declaramos animal e ingresamos la consola con input
animal = input("What is your favorite animal?  ")
#utilizamo format() par que demanera segura se ingrese los daots
# Para imprimir usando format() vamos a poner un {} por cada variable y el format() va a poner el valor de las variables en el orden que se estan usando
print("{}, you like a {} {}!".format(name,color,animal))


