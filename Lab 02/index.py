num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 == num2:
    print(f'{num1} and {num2} are equal')
elif num1 > num2:
    print(f'{num1} is greater than {num2}')
else:
    print(f'{num1} is smaller than {num2}')