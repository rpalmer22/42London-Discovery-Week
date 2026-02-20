#!/usr/bin/env python3

def array_of_names(dictionary):
    number_of_people=len(dictionary)
    output=[]
    first_name=list(dictionary.keys())
    second_name=list(dictionary.values())
    for i in range(number_of_people):
        full_name=first_name[i].capitalize() + " " + second_name[i].capitalize()
        #print(full_name)
        output.append(full_name)
    return(output)

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))
