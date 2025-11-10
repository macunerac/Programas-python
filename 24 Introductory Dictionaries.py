#Key/Value Structures

email = {  #Object email
    "From": "j.smith@example.com",
    "To": "zed.shaw@example.com",
    "Subject": "I HAVE AN AMAZING INVESTMENT FOR YOU!!!"};


print(email["From"]) ##Para imprimir el valor de la llave From
print(email["To"]) ##Para imprimir el valor de la llave To
print(email["Subject"]) ##Para imprimir el valor de la llave Subject


#-------------------------------------------------------------------------------------------

#Combining Lists with Data Objects

messages = [
    {"to": 'Sun', "from": 'Moon', "message": 'Hi!'},
    {"to": 'Moon', "from": 'Sun', "message": 'What do you want Sun?'},
    {"to": 'Sun', "from": 'Moon', "message": "I'm awake!"},
    {"to": 'hola', "from": 'Sun', "message": 'I can see that Sun.'}
]

#Accessing the data inside the list of dictionaries
# [0] dato o valor dentro es el numero de lista y el dato el segundo es la llave del diccionario
print(messages[0]['to']) # Moon 
print(messages[0]['from']) # Moon
print(messages[0]['message']) # Hi!
print(messages[1]['to']) # Moon
print(messages[1]['from']) # Sun
print(messages[1]['message']) # What do you want Sun?



