#!/usr/bin/env python3
import sys
number_of_parameters=len(sys.argv)-1
if number_of_parameters!=1:
    print("none")
else:
    output=sys.argv[1]
    print(output.upper())
    
    
