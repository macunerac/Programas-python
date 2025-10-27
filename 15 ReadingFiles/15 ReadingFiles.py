from sys import argv
script, filename = argv

txt = open(filename)

print(f"Here your file {filename}:")
print(txt.read())


print(f"Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

#Correr el script en CMD como abajo, El nombre del archivo es necesario ,Mi_archivo.txt, luego pedira
#otro nombre de otro archivo txt Mi_archivo-1.txt y mostara lo que se tiene adentro en cada archivo
#
#C:\Users\Humberto Molina\Desktop\Programas python\15 ReadingFiles>python ReadingFiles.py Mi_archivo.txt
#Here your file Mi_archivo.txt:
#Uno
#Dos
#File the filename again:
#> Mi_archivo-1.txt
#Tres
#Cuatro


