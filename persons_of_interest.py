#!/usr/bin/env python3

def famous_births(dictionary):
    tuples_sorted_by_date_values=sorted(dictionary.items(), key=lambda item: item[1]["date_of_birth"])
    sorted_dictionary=dict(tuples_sorted_by_date_values)
    #print(sorted_dictionary)
    number_of_entries=len(sorted_dictionary)
    for value in sorted_dictionary.items():
       print(f"{value[1]['name']} is a great scientist born in {value[1]['date_of_birth']}")

women_scientists={
    "ada": {"name": "Ada Lovelace", "date_of_birth": "1815"},
    "cecilia": {"name": "Cecilia Payne", "date_of_birth": "1900"},
    "lise": {"name": "Lise Meitner", "date_of_birth": "1878"},
    "grace": {"name": "Grace Hopper", "date_of_birth": "1906"}
}

famous_births(women_scientists)