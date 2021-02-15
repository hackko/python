#programa que reciba un valor entero ‘n’ e imprima como salida la serie de Fibonacci de 0 hasta el número n.

num = int(input("Ingrese el valor hasta donde desea la serie de fibonacci: "))

# primeros dos terminos
n1, n2 = 0, 1
cont = 0

# Checa si el valor introducido es valido
if num <= 0:
   print("Porfavor ingrese un numero positivo")
else:
   print("Secuencia Fibonacci:")
   while cont < num:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       cont += 1
