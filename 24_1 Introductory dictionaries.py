fruit = [{'kind': 'Apples','count': 12, 'rating': 'AAA'},
         {'kind': 'Oranges', 'count': 1, 'rating': 'B'},
         {'kind': 'Pears','count': 2, 'rating': 'A'},
         {'kind': 'Grapes','count': 14, 'rating': 'UR'}
         ];

cars = [
    {'type': 'Cadillac', 'color': 'Black','size': 'Big', 'miles': 34500},
    {'type': 'Corvette', 'color': 'Red','size': 'Little', 'miles': 1000000},
    {'type': 'Ford', 'color': 'Blue','size': 'Medium', 'miles': 1234},
    {'type': 'BMW', 'color': 'White','size': 'Baby', 'miles': 7890}
    ];


languages = [
    {'name': 'Python', 'speed': 'Slow','opinion': ['Terrible', 'Mush']},
    {'name': 'JavaScript', 'speed': 'Moderate','opinion': ['Alright', 'Bizarre']},
    {'name': 'Perl6', 'speed': 'Moderate','opinion': ['Fun', 'Weird']},
    {'name': 'C', 'speed': 'Fast','opinion': ['Annoying', 'Dangerous']},
    {'name': 'Forth', 'speed': 'Fast','opinion': ['Fun', 'Difficult']},
    ];

#Fruit challenge
print
print(fruit[0]['count'])  # 12
print(fruit[0]['rating'])  # AAA
print(fruit[2]['count'])  # 2
print(fruit[1]['kind'])  # Oranges
print(fruit[3]['kind'])  # Grapes
print(fruit[3]['count']) # 14
print(fruit[0]['kind']) # Apples

#Cars challenge
print("Cars challenge\n")
print(cars[0]['size'])  # Big
print(cars[1]['color'])  # Red
print(cars[2]['miles'])  # 1234
print(cars[3]['color'])  # White
print(cars[3]['miles']) # 7890  
print(cars[0]['color']) # Black
print(cars[0]['miles']) # 34500
print(cars[2]['color']) # Blue  

#Language challenge
print("Language challenge\n")   
print(languages[0]['speed'])  # Slow
print(languages[1]['opinion'][0])  # Alright
print(languages[3]['opinion'][1])  # Dangerous
print(languages[4]['speed'])  # Fast        
print(languages[4]['opinion'][1])  # Difficult
print(languages[4]['opinion'][0])  # Fun    
print(languages[3]['opinion'][0]) # Annoying
print(languages[2]['opinion'][1])    # Weird
print(languages[1]['speed'])    # Moderate
