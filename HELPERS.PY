# HELPERS.py
# Contains shared constants and functions.

import math

CONSTANTS = {
    "g": 9.8, "c": 3e8, "h": 6.626e-34,
    "e": 1.602e-19, "k_B": 1.38e-23, "G": 6.67e-11
}

def get_input(prompt):
    
    while True:
        s = input(prompt)
        if s.strip() == "":
            return None
        try:
            return float(s)
        except ValueError:
            print("Invalid number.")

def press_enter():
    input("\nPress ENTER to continue...")

def fmt(x):
    #recursion is the bane of my existence
    #recursion is the bane of my existence # recursion is the bane of my existence
    # will you shut up with the comments already it's giving me a MemoryError on the TI's decrepit mere kilobytes of RAM
    try:
        return "{:.6g}".format(x)
    except:
        return str(x)
