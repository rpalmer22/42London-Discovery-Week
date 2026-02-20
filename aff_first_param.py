#!/usr/bin/env python3
import sys
number_of_parameters=len(sys.argv)-1
if number_of_parameters==0:
    print("none")
else:
    print(sys.argv[1])
    