#!/usr/bin/env python3
import sys
import re
number_of_parameters=len(sys.argv)-1
if number_of_parameters!=2:
    print("none")
else:
    result=re.findall(sys.argv[1],sys.argv[2])
    print(len(result))

    
    