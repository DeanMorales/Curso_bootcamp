#-----------------laboratorio 7 ---------------------------
#se va a crear un condicional para validar si puedes entrar o no a una fiesta
#se declara lavariable edad que guarda dendo el input que nosotros definamos en consola
edad = input("escriba su edad: ")
#combertimos la variable entrada a entero debido a que con inputo el valor que se guarda es un texto
edad = int(edad)
#se comprar con la desicion if
if edad>=18 : 
    # TODO: write code...
    print("puede entrar")
else:
# sino se cumple la condicion de ser 18 años entonces:
    print("no puede entrar")

#ahora se va a validar si la persona es mayor de edad y si ademas tiene mas de 600 pesos 
edad = input("escriba su edad: ")
edad = int(edad)
dinero = input("escriba su dinero: ")
dinero = int(dinero)
#se comprar con la desicion if
if edad>=18 : 
    # TODO: write code...
    if edad >= 600: 
        print("verificamos si cuenta con el dinero")
    else:
        print("no tiene el dinero suficiente no puede entrar")
else:
# sino se cumple la condicion de ser 18 años entonces:
    print("como no tiene la edad no puede entrar")

#version 2 mejorado     
if edad>=18 and dinero >= 600:
    print("verificamos si tiene la edad y cuenta con el dinero")
else:
    # sino se cumple la condicion de ser 18 años entonces:
    print("como no tiene la edad no puede entrar")

#******************************************************************    
#condicional con multiples comparaciones
#creamos la variable llamada dinero
dinero=input("escriba el diner con el que cuenta: ")
#convertimos la variable string a entero
dinero= int(dinero)

if dinero   < 100 : 
    print("le compro unas galletas")
elif dinero >= 100 and dinero <=200:
    print("le compro unos chocolate")
elif dinero >= 200 and dinero <=300:
    print("le compro unas picafresas")
else:
    print("le compro una moto")

#--------------------------------------laboratorio--------------------------------------------

#se le pide al usuario responder con yes or no 
userReply = input("Do you need to ship a package? (Enter yes or no) ")
if userReply == "yes":
    print("We can help you ship that package!")
else:
    print("Please come back when you need to ship a package. Thank you.")
#
userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")
if userReply == "stamps":
    print("We have many stamp designs to choose from.")
elif userReply == "envelope":
    print("We have many envelope sizes to choose from.")
elif userReply == "copy":
    #se crea ka varaible copias, y si imprimie el numero de copias
    copies = input("How many copies would you like? (Enter a number) ")
    print("Here are {} copies.".format(copies))
else:
    #se imprime el mensaje de despedida 
    print("Thank you, please come again.")