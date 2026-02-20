#!/usr/bin/env python3
import sys
number_of_parameters=len(sys.argv)-1
if number_of_parameters!=1:
    print("none")
else:
    passcode=sys.argv[1]
    guess=input("What was the parameter? ")
    if guess==passcode:
        print("Good job!")
    else:
        print("Nope, soz mate...")
