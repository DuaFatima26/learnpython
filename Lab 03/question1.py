# Task 1: Multiplication Table
num = int(input("Enter a number to create its multiplication table: "))

print(f"\nMultiplication table of {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")