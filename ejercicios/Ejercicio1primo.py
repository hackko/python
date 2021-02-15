
#Programa para que reciba un número entero y de como salida la respuesta a si el número recibo es un número primo o no.

# -*- coding: utf-8 -*-

def esPrimo(num):
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

def programa():
    num = int(input('Escribe un Numero: '))
    resultado = esPrimo(num)

    if resultado is True:
        print('Este numero es primo!!')
    else:
        print('Este numero no es primo!!')

if __name__ == '__main__':
    programa()
