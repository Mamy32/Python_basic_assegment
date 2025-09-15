print("Question 1: ")
print("Put your first number: ", end = " ")
number1 = int(input())
print("Put your second number: ", end = " ")
number2 = int(input())

print(f"Adding: {number1} + {number2} = {number1+number2}")
print(f"Subtracting: {number1} - {number2} = {number1-number2}")

print("Question 2: ")
print(f"Multiplying: {number1} * {number2} = {number1*number2}")
print(f"Dividing: {number1} / {number2} = {number1/number2}")

print("Question 3: ")
print("Put your first number: ", end = " ")
number1 = int(input())
print("Put your second number: ", end = " ")
number2 = int(input())
print("Put your third number: ", end = " ")
number3 = int(input())
print(f"The result of ({number1} + {number2}) / {number3} = {(number1+number2)/number3}")

print("Question 4: ")
print("Put your first number: ", end = " ")
number1 = int(input())
print("Put your second number: ", end = " ")
number2 = int(input())

if number1 >= number2:
    print(True)
else:
    print(False)

