# Project 9

height = float(input("Please enter your height input meters(decimals): "))
weight = int(input('Please enter your weight input kg: '))
bmi = weight/(height*height)
if bmi <= 18.5:
        print('Your BMI is', bmi,'which means you are underweight.')

elif bmi > 18.5 and bmi < 25:
        print('Your BMI is', bmi,'which means you are normal.')

elif bmi > 25 and bmi < 30:
        print('your BMI is', bmi,'overweight.')
        
elif bmi > 30:
        print('Your BMI is', bmi,'which means you are obese.')

else:
        print('There is an error with you inputput')
        print('Please check you have entered whole numbers\n'
              'and decimals where asked.')
