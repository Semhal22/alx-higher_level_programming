#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    biggest_score = 0
    for key, value in a_dictionary.items():
        if value > biggest_score:
            biggest_score = value
            best = key
    return best
