#!/usr/bin/env python3
import sys
number_of_parameters=len(sys.argv)-1
if number_of_parameters==0:
    print("none")
else:
    print(f"parameters: {number_of_parameters}")
    for i in range(number_of_parameters):
        print(f"{sys.argv[i+1]} : {len(sys.argv[i+1])}")
              