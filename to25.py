#!/usr/bin/env python3
number = int(input("Enter a number less than 25 \n"))
if number > 25:
    print("Error")
else:
    while number < 26:
        print("Inside the loop, my variable is " + str(number))
        number = number +1
