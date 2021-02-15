# -*- coding: utf-8 -*-

# Ejercicio 4

"""
Dado el siguiente diccionario, genera un programa que reciba dos números ‘x’ y ‘y’, posteriormente entrega como salida el mismo diccionario donde la llave “a” tendrá su contenido original más ‘x’ y la llave ‘b’ tendrá su contenido original más ‘y’.


"""


x = int(input ("Ingresa el dato x "))
y = int(input ("Ingresa el dato y "))

CMD = { "ID": 55, "Data": "hola", "More": [ { "a": 1 }, {"b":2 }]}

print ("CMD = " , end="")
print (CMD)

CMD ["More"][0].update ({"x": x})
CMD ["More"][1].update ({"y": y})


print ("CMD = " , end="")
print (CMD)
