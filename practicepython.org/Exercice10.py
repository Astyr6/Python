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


for i in range(1,17):
    c = random.choice(range(1,10))
    if c >= 1 and c <= 3:
        pwgen += random.choice(lowercaseAlphabet)
    if c >= 4 and c <= 6:
        pwgen += random.choice(uppercaseAlphabet)
    if c >= 7 and c <= 8:
        pwgen += random.choice(numbers)
    if c >= 8 and c <= 9:
        pwgen += random.choice(symbols)

print(standardPassword())