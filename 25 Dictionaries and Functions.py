#Step 1: Function Names Are Variables

def print_number(x):
    print("NUMBER IS", x)
    rename_print = print_number
    rename_print(100)
    print_number(100)
    

    x = 10
    y = x

#---------------------------------------------------------------------------

#Step 2: Dictionaries with Variables

color = "Red"

corvette = {
    "color": color
    }

print("LITTLE", corvette["color"], "CORVETTE")

#---------------------------------------------------------------------------
#Step 3: Dictionaries with Functions


def run():
    print("VROOM")

corvette = {
    "color": "Red",
    "run": run
    }

print("My", corvette["color"], "can go")
corvette["run"]()  #Imprime lo que tiene la funciòn run en el print osea decir VROOM

#---------------------------------------------------------------------------
#Step 4: Deciphering the Last Line

# get the run fuction out of the corvette dict
myrun = corvette["run"] #Imprime lo que guarda la lista corvette osea decir VROOM
# run it
print(myrun()) ##Imprime None porque la variable myrun no tiene ningun valor asignado
myrun() #Imprime VROOM porque myrun tiene asignada la funciòn run
