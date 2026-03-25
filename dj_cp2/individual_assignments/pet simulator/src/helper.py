import sys
import time

def clear_screen():
    print("\033c", end="")

def continue_screen():
    print("Press Enter to continue.")
    input()

def after_action():
    continue_screen()
    clear_screen()

# make sure values can't go too high or too low
def max_min_checker(value):
    if value > 100:
        value = 100
    elif value < 0:
        value = 0
    else:
        pass

    return value

# this is used for adding, saving, or deleting things from the CSV files
def find_dict_index(list_of_dicts, key, value):
    for index, d in enumerate(list_of_dicts):
        if d.get(key) == value:
            return index  
    return -1  