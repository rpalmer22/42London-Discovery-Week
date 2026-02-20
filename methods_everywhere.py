#!/usr/bin/env python3
import sys

def shrink(string):
    subset=string[0:8]
    print(subset)

def enlarge(string):
    length=len(string)
    for i in range(8-length):
        string=string+'Z'
        #string += 'Z'
    print(string)

number_of_parameters=len(sys.argv)-1
if number_of_parameters==0:
    print("none")
else:
    for i in range(number_of_parameters):
        number_of_characters=len(sys.argv[i+1])
        if number_of_characters==8:
             print(sys.argv[i+1])
        elif number_of_characters>8:
             shrink(sys.argv[i+1])
        else:
             enlarge(sys.argv[i+1])
