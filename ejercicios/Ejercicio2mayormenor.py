#programa que recibe como entrada una lista de n números y de como salida los dos números más chicos y los dos números más grandes.

lista = []
cantidad = int (input("Cantidad de numero a digitar: "))
ma = 0
ma1 = 0
me = 0
me1 = 0
i= 1


while (cantidad > 0):
    numero = int (input ("Numero  # "+ str (i) + ": "))
    lista.append (numero)
    i = i + 1
    cantidad = cantidad - 1

ma = max (lista)
me = min(lista)

def seg_menor(numeros):
    if isinstance(numeros, list):
        if len(numeros) < 2:
            return None
        if len(numeros) == 2 and numeros[0] == numeros[1]:
            return numeros[0]
        duplicados = set()
        unicos = []

        for n in numeros:
            if n not in duplicados:
                duplicados.add(n)
                unicos.append(n)

        unicos.sort()

        return unicos[1]

    raise TypeError('El parámetro numeros debe ser una lista')

def seg_mayor(numeros):

    if isinstance(numeros, list):
        if len(numeros) < 2:
            return None
        if len(numeros) == 2 and numeros[0] == numeros[1]:
            return numeros[0]
        duplicados = set()
        unicos = []

        for n in numeros:
            if n not in duplicados:
                duplicados.add(n)
                unicos.append(n)

        unicos.sort(reverse=True)

        return unicos[1]

    raise TypeError('El parámetro numeros debe ser una lista')

ma1 = seg_mayor(lista)
me1 = seg_menor(lista)

print ("Lista : ", lista)
print ("Mayor : ", ma)
print ("Segundo mayor: ", ma1)
print ("Menor : ", me)
print ("Segundo menor : ", me1)
