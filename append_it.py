#!/usr/bin/env python3
import sys
import re
number_of_parameters=len(sys.argv)-1
if number_of_parameters==0:
    print("none")
else:
    for i in range(number_of_parameters):
        string=sys.argv[i+1]
        ending=string.find("ism", len(string)-3)
        if ending==-1:
            print(sys.argv[i+1]+"ism")
    

