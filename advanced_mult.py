#!/usr/bin/env python3
starting_int = 0
while starting_int < 11:
    print("Table of " + str(starting_int) + ": ", end="")
    multiplier = 0
    while multiplier < 11:
        result = starting_int * multiplier
        print(str(result), end=" ")
        multiplier = multiplier + 1
    starting_int = starting_int + 1
    print()


    
    