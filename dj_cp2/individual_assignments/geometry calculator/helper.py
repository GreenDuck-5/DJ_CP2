import sys
import time

def clear_screen(): 
    print("\033c", end = "")

def continue_screen(): 
    input("Press \"Enter\" or \"Return\" to continue:\n")

def print_slow(text):
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.02)
    print()

