from sys import argv

script, user_name = argv
prompt = '> '

print(f"Hi {user_name}, I`m the {script} script.")
print("I`d like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
      Alright, so you said {likes} about liking me.
      You live in {lives}. Not sure where that is.
      And you have a {computer}. Nice.      
      """)


#Correr el script en CMD como abajo, Humberto es el dato que es necasrio para que no de error
#python "C:\Users\Humberto Molina\Desktop\Programas python\13 Parameters,Unpacking, Vaiables.py" Humberto

#Mostrara esto
#C:\Users\Humberto Molina\Desktop\Programas python>python "14 Prompting and Passing.py" Humberto
#Hi hHumberto, I`m the 14 Prompting and Passing.py script.
#I`d like to ask you a few questions.
#Do you like me Humberto?
#> Como hacer comida
#Where do you live hola
#> mexico
#What kind of computer do you have?
#> laptop

#      Alright, so you said Como hacer comida about liking me.
#      You live in mexico. Not sure where that is.
#      And you have a laptop. Nice.
