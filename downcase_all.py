#!/usr/bin/env python3
import sys

number_of_parameters=len(sys.argv)-1

def downcase_it(string):
    return string.lower()


if number_of_parameters==0:
    print("none")
else:
    for i in range(number_of_parameters):
        print(downcase_it(sys.argv[i+1]))
        