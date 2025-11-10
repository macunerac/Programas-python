#Step 1: Review of import ,llama al módulo ex26.py y accede a sus variables.

import ex26

print("name", ex26.name)
print("height", ex26.height)


from pprint import pprint
pprint(ex26.__dict__)

#____________________________________________________________________________________________________________
#Step 2: Find the __dict__


#ex26.height 👉 es la forma normal y sencilla.
#ex26.__dict__['height'] 👉 es la forma interna y técnica, útil cuando quieres manipular dinámicamente los nombres de atributos.


#La función pprint() sirve para mostrar el contenido de un diccionario de forma más legible.
#Cuando la usas con un módulo, puedes ver que este tiene una variable “oculta” llamada __dict__, 
#que es literalmente un diccionario con todo lo que contiene el módulo (funciones, variables, etc.).

#Aunque muchos programadores no lo notan, un módulo en Python internamente es como un diccionario.
#La diferencia es que Python permite acceder a sus elementos con el punto (modulo.funcion) en lugar de usar la 
#sintaxis de diccionario (modulo.__dict__['funcion']).

print("height is", ex26.height)
print("height is also", ex26.__dict__['height'])

#____________________________________________________________________________________________________________
#Step 3: Change the __dict__

print(f"I am currently {ex26.height} inches tall.")

ex26.__dict__['height'] = 1000  ##cambia la variable height en el módulo ex26 a 1000
print(f"I am now {ex26.height} inches tall.")

ex26.height = 12 ##cambia la variable height en el módulo ex26 a 12
print(f"Oops, now I'm {ex26.__dict__['height']} inches tall.")