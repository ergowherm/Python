# Python Identity Operators
# Assume two Variables a and b

a = 20
b = 20

print('Line 1', 'a=', a , ':', id(a), 'b=', b, ':', id(b))

if (a is b):
    print("Line 2 -- Varbles are identitical")
else:
    print("Line 2 --- Variable are not Identical")

if ( id(a) == id(b) ):
    print("Output --  a and b are identical")
else:
    print("output -- a and b are not identical")

    b=30
    
if ( a is not b):
    print("Line 3 --  a and b are not identical")
else:
    print("Line 3 -- a and b are identical")

# Example

    age1 = 27
    age2= 19




    
    
