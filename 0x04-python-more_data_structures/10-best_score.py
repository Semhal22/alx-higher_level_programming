#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    biggest_score = 0
    biggest_key = None
    for key, value in a_dictionary.items():
        if value > biggest_score:
            biggest_score = value
            biggest_key = key
    return biggest_key
