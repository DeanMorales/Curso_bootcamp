#siempre que importemos una libreria debe ir al principio del codigo
import random
#-------------laboratorio 8 --------------------------
#un ciclo while es un bulque que va a recorrer hasta que no se cumpla la condicion
#numero igual 
numero  = input("ingresa un numero 0: ")
#convertimos la variable a numero entereo con int()
numero= int(numero)
while numero < 10:
    print(numero)
    numero= numero +1 

#---------------------------------------------------------------------------
numero  = input("ingresa un numero 0: ")
#convertimos la variable a numero entereo con int()
numero = int(numero)
multipicador = 0
while multipicador < 10:
    multipicador= multipicador +1
    multiplicacion=multipicador*numero
    #se aplica formato para multiplicacion
    print("{} x {} = {}".format(numero, multipicador, multiplicacion))
#----------------laboratorio 8-------------------------------------
#se realizan 2 impresiones
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")
#la libreria random genera un numero aleatorio entre el numer 1 y 10 como se define acontinuacion
number = random.randint(1,10)
#
isGuessRight = False
#entra al ciclo while porque la variable isGuessRight  es diferente de true
while isGuessRight != True:
    #pide al usuario que ingrese un  numero entre 1 y 10
    guess = input("Guess a number between 1 and 10: ")
    #si la variable guess es igual a number que fue el numero gennerado aleatoriamente 
    if int(guess) == number:
        #imprime que ganaste 
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    #si es falso dara el siguiente mensaje en consola y se repetira la primera intruccion del while
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))