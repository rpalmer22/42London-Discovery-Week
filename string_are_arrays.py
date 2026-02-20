#!/usr/bin/env python3
import sys
import re
number_of_parameters=len(sys.argv)-1
if number_of_parameters!=1:
    print("none")
else:
    result=re.findall('z', sys.argv[1])
    number=len(result)
    if number==0:
        print("none")
    else:
        for i in range(number):
            print("z", end="")
        print()
