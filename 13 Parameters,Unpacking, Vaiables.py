from sys import argv

#r read the WYSS section for how to run this
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

#Correr el script en CMD como abajo
#python "C:\Users\Humberto Molina\Desktop\Programas python\13 Parameters,Unpacking, Vaiables.py" first second ters

#NOTA:  argv sirve para recibir valores que el usuario pasa al programa desde la línea de comandos (la terminal).
#El nombre viene de “argument vector” → es una lista de argumentos que el intérprete de Python recibe cuando se ejecuta el script.