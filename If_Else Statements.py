#  Python 3 -- Decision Making
# Consider  one vaiable a = 50

# if Statement

a = 50
if (a >= 50):
    print("Student is Passed with Grade C")
else:
    print("Student is failed")

# Example

amount = int (input ("Enter the Amount:"))

if amount <= 1000:
    discount = amount * 0.05
    print ("Discount is",discount)
else:
    discount = amount * 0.10
    print("Discount is ", discount)

print("Total Amount to Pay is here:", amount - discount)

# Example if else 

# if the user ammount is > = 10000 provide 20 % discount else
 # 10 %

amt = int (input ("Please enter the amount:" ))
if amt >=  10000:
      dcount = amt * 0.20
      print("Discount amount is:", dcount)
else:
    dcount= amt * 0.10
    print("Discount amount is :", dcount)

print("Total amount after Discount:", amount-dcount)
      
# Example if elif

amount=int(input("Enter amount: "))
if amount<1000:
    discount=amount*0.05
    print ("Discount",discount)
elif amount<5000:
    discount=amount*0.10
    print ("Discount",discount)
else:
    discount=amount*0.15
    print ("Discount",discount)
    
print ("Net payable:",amount-discount)
              



























 

