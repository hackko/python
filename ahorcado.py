#-*- coding: utf-8 -*-

# Juego del Ahorcado
"""
Este es un programa que realiza la ejecucion del juego del Ahorcado en el cual colocas la palabra a adivinar y tienes 5 intentos para adivinar la palabra
"""

import time;
print("Hola, es hora de jugar Ahorcado")
print("")
palabra=list(input("Coloca la palabra a adivinar "))
print("")
time.sleep(1)
print (type(palabra))
print (palabra)
print("Comienza a adivinar")
time.sleep(0.5)
tupalabra=""
vidas=5


while vidas > 0:
    fallas=0
    for letra in palabra:
        if letra in tupalabra:
            print(letra,end="")
        else:
            print("_",end="")

            fallas+=1
    if fallas==0:
        input()
        print("")
        print("Felicidades, ganaste")
        input()
        break
    print ("")
    tuletra=input("Introduce una letra: ")
    tupalabra+=tuletra

    if tuletra not in palabra:
        vidas-=1
        print("Te equivocaste")
        print("Tu tienes ",+vidas," vidas")
    if vidas== 0:
        print("Perdiste!")
else:
    print("Gracias por participar")
