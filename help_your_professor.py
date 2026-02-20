#!/usr/bin/env python3

def average(dictionary):
    number_of_students=len(dictionary)
    #print(f"Number of students is {number_of_students}")
    total_score=sum(dictionary.values())
    return total_score/number_of_students

class_3B = {
    "marine": 18,
    "jean": 15,
    "coline": 8,
    "luc": 9
}

class_3C = {
    "quentin": 17,
    "julie": 15,
    "marc": 8,
    "stephanie": 13
}

print(f"Average for Class 3B: {average(class_3B)}.")
print(f"Average for Class 3C: {average(class_3C)}.")