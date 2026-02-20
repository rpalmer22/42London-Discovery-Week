#!/usr/bin/env python3

def find_the_reheads(dictionary):
    filtered_items=filter(lambda item: item[1]=="red", dictionary.items())
    filtered_keys=[item[0] for item in filtered_items]
    filtered_dict=list(filtered_keys)
    print(filtered_dict)


dupont_family={
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

find_the_reheads(dupont_family)