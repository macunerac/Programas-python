from sys import argv
input_file = "ex20_test.txt"

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)


def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole file:\n")
print_all(current_file)

print("Now let's rewind, kind of like a tape.")
rewind(current_file)

print("Let's print three lines:")

current_line = 1 #Guarda 1 al inicio de la linea
print_a_line(current_line, current_file)

current_line = current_line + 1 #Guarda 2 al inicio de la linea
print_a_line(current_line, current_file)

current_line = current_line + 1  #Guarda 3 al inicio de la linea
print_a_line(current_line, current_file) 

#You’ll also need a file named ex20_test.txt with the following contents:
#This is line 1
#This is line 2
#This is line 3