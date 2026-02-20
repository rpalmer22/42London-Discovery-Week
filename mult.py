#!/usr/bin/env python3
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
result = first_number * second_number
print(str(first_number) + " x " + str(second_number) + " = " + str(result))
if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")
