#!/usr/bin/env python3
import sys
number_of_parameters=len(sys.argv)-1
if number_of_parameters<2:
    print("none")
else:
    x=number_of_parameters
    while x>=0:
        print(sys.argv[x])
        x=x-1
