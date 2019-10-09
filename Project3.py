def main():
    enter code herescores = input("Enter five test scores seperated by commas:")
    listScores = scores.split(",")`enter code here`
    determine_grade(listScores)
    calc_average(listScores)

def determine_grade(grades):
    for num in grades:
        if int(num) >= 90 and int(num) <= 100:
            print("A")
        elif int(num) >=80 and int(num) <= 89:
            print("B")
        elif int(num) >=70 and int(num) <= 79:
            print("C")
        elif int(num) >=60 and int(num) <= 69:
            print("D")
        else:
            print("F")


def calc_average(grades):
    total = 0
    for num in grades:
        total += int(num)
    average = total / 5
    print(average)
