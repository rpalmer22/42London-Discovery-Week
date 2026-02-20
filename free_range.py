#!/usr/bin/env python3
import sys
number_of_parameters=len(sys.argv)-1
if number_of_parameters!=2:
    print("none")
else:
    first_number=int(sys.argv[1])
    second_number=int(sys.argv[2])
    if first_number>=second_number:
        print("The first number must be smaller than the second number")
    else:
        numbers=list(range(first_number,second_number+1,1))
        print(numbers)