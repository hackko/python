#Ejercicio 5
"""
Genera un programa que realice lo siguiente,
-	Tenga una clase de tipo Pokemon con los atributos DEFENSA, ATAQUE y RAPIDEZ, y un método GRUÑIDO que imprima el sonido que hace el pokemon en minúsculas.
-	Instancia la clase generando al menos 3 pokemones, puedes agregar el valor que gustes para cada uno de sus atributos.
-	Genera una clase hija de la clase pokemon llamada PKMGEN2 que sobreescriba el método GRUÑIDO para imprimir el sonido que hace el pokemon en mayúsculas.
-	Instancia la nueva clase y genera un nuevo pokemon.
"""





class Pokemon:

        def __init__(self,nombre, defensa, ataque, rapidez):
            self.nombre = nombre
            self.defensa = defensa
            self.ataque = ataque
            self.rapidez = rapidez
            print(f"Este es el pokemon {self.nombre} , Defensa : {self.defensa}, Ataque:  {self.ataque}, Rapidez {self.rapidez}")

        def grunido (self):

            print ("rrrrrrrrrrr")


class PKMGEN2(Pokemon) :

        def grunido (self):
            print ("RRRRRRRRRRR")




Squirtle = PKMGEN2 ('Squirtle', 100, 5, 30)
Squirtle.grunido()
Bulbasaur = PKMGEN2('Bulbasaur', 100, 10, 60)
Bulbasaur.grunido()
Pikachu = Pokemon('Pikachu', 100, 80, 60, )
Pikachu.grunido()
