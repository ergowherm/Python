# Lambda Funtions with def()

def cube(x):
    return x * x * x;

num = lambda a : a*a*a
print (num(3))

print (cube(7))

# lambda

age = lambda a : a + 4
print (age(24))

# add more arguments

add = lambda a , b , c : a + b + c
print (add (100, 200, 600))

#

def func (x):
    return lambda a : a * x

value = func(4)

print (value (11))



# Classes

class myclass:
    x = 18

print myclass


















