import random

lowercaseAlphabet = "abcdefghijklmnopqrstuvwxyz"
uppercaseAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "~`!@#$%^&*()_-+={[}]|\:;\"'<,>.?/"
pwgen = ""

def veryWeakPassword(length = 8):
    pw = ""
    for i in range(1, length + 1):
        pw += random.choice(lowercaseAlphabet)
    return pw

def weakPassword(length = 12):
    pw = ""
    for i in range(1, length + 1):
        c = random.choice(range(1,4))
        if c <= 2:
            pw += random.choice(lowercaseAlphabet)
        else:
            pw += random.choice(uppercaseAlphabet)
    return pw

def standardPassword(length = 16):
    pw = ""
    for i in range(1, length + 1):
        c = random.choice(range(1,7))
        if c <= 3 and c < 3:
            pw += random.choice(lowercaseAlphabet)
        elif c > 3 and c < 6:
            pw += random.choice(uppercaseAlphabet)
        elif c == 6:
            pw += random.choice(numbers)
    return pw

def strongPassword(length = 16):
    pw = ""
    for i in range(1, length + 1):
        c = random.choice(range(1,9))
        if c <= 3 and c < 3:
            pw += random.choice(lowercaseAlphabet)
        elif c > 3 and c < 6:
            pw += random.choice(uppercaseAlphabet)
        elif c == 6 or c == 7:
            pw += random.choice(numbers)
        elif c == 8:
            pw += random.choice(symbols)
    return pw

def superStrongPassword(length = 20):
    pw = ""
    for i in range(1, length + 1):
        c = random.choice(range(1,11))
        if c <= 3 and c < 3:
            pw += random.choice(lowercaseAlphabet)
        elif c > 3 and c < 6:
            pw += random.choice(uppercaseAlphabet)
        elif c == 6 or c == 7 or c == 8:
            pw += random.choice(numbers)
        elif c > 8:
            pw += random.choice(symbols)
    return pw



print(superStrongPassword())