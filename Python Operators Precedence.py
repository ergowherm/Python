#Python Operators Precedence
a =50
b = 60
c = 70
d = 90

print("a:%d, b:%d, c:%d, d:%d" % (a,b,c,d ))

output = (a + d/c * b)
print("The output is:", output)

result = (a + b) * c / d

print("The Answer is:", result)

result2 = ((a + b) * c) / d

print("The Result is :", result2)

Weight1 = (a + b) * (c / d)
print("The Weight of this machine is: ", Weight1)

Weight2 = a + (b * c) / d
print("The Weight of Server machine is: ", Weight2)
