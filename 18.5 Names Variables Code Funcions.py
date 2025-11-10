def do_more_things(a, b):
    a = "hello"
    b = 1
    print("A IS", a, "B IS", b)


#I have two arguments (also called “parameters”) to the do_more_things() function: a
#and b. When I call this function using do_more_things("hello", 1), Python temporarily assigns
#a="hello" and b=1 and then calls the function. That means, inside the function a and b will have those
#values, and they’ll disappear when the function exits
