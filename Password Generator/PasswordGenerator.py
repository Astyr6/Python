from getpass import getpass
import random
import os
import pyperclip
from typing import DefaultDict

clear = lambda: os.system("cls")

# LISTS

lowercaseAlphabet = "abcdefghijklmnopqrstuvwxyz"
uppercaseAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "~`!@#$%^&*()_-+={[}]|\:;\"'<,>.?/"
pwgen = ""


# GUI FUNCTIONS

def gui_header():
    print("==================================================")
    print("Password Generator")
    print("==================================================")
    print("")


def gui_list():
    print("Password strength :")
    print("(1) Very weak")
    print("(2) Weak")
    print("(3) Standard")
    print("(4) Strong")
    print("(5) Super strong")
    print("-------------------")
    print("(6) Custom")
    print("-------------------")
    print("(0) Quit")
    print("")


# INPUT HANDLING FUNCTIONS

def int_input(text, default):
    max_tries = 3
    while max_tries > 0:
        result = input(text).strip()

        if not result:
            return default

        try:
            return int(result)
        except ValueError:
            max_tries -= 1
            print("Bad value: {!r}. Try again...".format(result))


def bool_input(text, default):
    max_tries = 3
    while max_tries > 0:
        result = input(text).strip()

        if not result:
            return default

        try:
            return {"Y": True, "N": False}[result.upper()]
        except KeyError:
            max_tries -= 1
            print("Bad value: {!r}. Try again...".format(result))


# PASSWORD FUNCTIONS

def veryWeakPassword():
    length = int_input("Length ? (Default 8) > ", 8)
    pw = ""
    for i in range(1, length + 1):
        pw += random.choice(lowercaseAlphabet)
    str_var = list(pw)
    random.shuffle(str_var)

    return "".join(str_var)


def weakPassword():
    length = int_input("Length ? (Default 8) > ", 8)
    pw = ""
    for i in range(1, length + 1):
        pw += random.choice(lowercaseAlphabet + uppercaseAlphabet)

    str_var = list(pw)
    random.shuffle(str_var)

    return "".join(str_var)


def standardPassword():
    length = int_input("Length ? (Default 12) > ", 12)
    pw = ""
    for i in range(1, length + 1):
        c = random.choice(range(1, 7))
        if c in range(1, 4):
            pw += random.choice(lowercaseAlphabet)
        elif c in range(4, 6):
            pw += random.choice(uppercaseAlphabet)
        elif c == 6:
            pw += random.choice(numbers)
    str_var = list(pw)
    random.shuffle(str_var)

    return "".join(str_var)


def strongPassword():
    length = int_input("Length ? (Default 16) > ", 16)
    pw = ""
    for i in range(1, length + 1):
        c = random.choice(range(1, 9))
        if c in range(1, 4):
            pw += random.choice(lowercaseAlphabet)
        elif c in range(4, 6):
            pw += random.choice(uppercaseAlphabet)
        elif c in range(6, 8):
            pw += random.choice(numbers)
        elif c == 8:
            pw += random.choice(symbols)

    str_var = list(pw)
    random.shuffle(str_var)

    return "".join(str_var)


def superStrongPassword():
    length = int_input("Length ? (Default 32) > ", 32)
    pw = ""
    for i in range(1, length + 1):
        c = random.choice(range(1, 11))
        if c in range(1, 3):
            pw += random.choice(lowercaseAlphabet)
        elif c in range(3, 6):
            pw += random.choice(uppercaseAlphabet)
        elif c in range(6, 9):
            pw += random.choice(numbers)
        elif c in range(9, 11):
            pw += random.choice(symbols)

    str_var = list(pw)
    random.shuffle(str_var)

    return "".join(str_var)


def customPassword():
    length = 16
    uppercase = True
    number = True
    symbol = False
    numOfNumbers = 2
    numOfSymbols = 2

    length = int_input("Length ? (Default 16) > ", 16)

    uppercase = bool_input("Uppercase Letters ? (Default Yes) Y or N > ", True)

    number = bool_input("Numbers ? (Default Yes) Y or N > ", True)

    symbol = bool_input("Symbols ? (Default No) Y or N > ", False)

    if number:
        numOfNumbers = int_input("Number of numbers ? (Default 2, Max = Length / 2) > ", 2)
    if numOfNumbers > length / 2:
        numOfNumbers = length // 2

    if symbol:
        numOfSymbols = int_input("Number of Symbols ? (Default 2, Max = Length / 2) > ", 2)
    if numOfSymbols > length / 2:
        numOfSymbols = length // 2

    pw = ""

    if number and numOfNumbers <= length / 2:
        for i in range(1, numOfNumbers + 1):
            pw += random.choice(numbers)

    if symbol and numOfSymbols <= length / 2:
        for i in range(1, numOfSymbols + 1):
            pw += random.choice(symbols)

    for i in range(1, length - (len(pw) + 1)):
        if uppercase:
            pw += random.choice(lowercaseAlphabet + uppercaseAlphabet)
        else:
            pw += random.choice(lowercaseAlphabet)

    str_var = list(pw)
    random.shuffle(str_var)

    return "".join(str_var)


# =========
# MAIN CODE
# =========

while True:

    clear()

    gui_header()

    gui_list()

    ipt = int()

    try:
        ipt = int(input("Choice > "))
    except ValueError:
        continue

    print("")

    gened = ""
    if ipt == 1:
        gened = veryWeakPassword()
    elif ipt == 2:
        gened = weakPassword()
    elif ipt == 3:
        gened = standardPassword()
    elif ipt == 4:
        gened = strongPassword()
    elif ipt == 5:
        gened = superStrongPassword()

    elif ipt == 6:
        gened = customPassword()

    elif ipt == 0:
        break

    print("")
    print(gened)
    print("")

    clip = bool_input("Copy to clipboard ? (Default N) Y or N > ", False)

    if clip:
        pyperclip.copy(gened)
        print("Copied to clipboard !")

    print("")
    getpass("Press Enter to continue...")
