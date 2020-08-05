import os

import pyAesCrypt as Aes

clear = lambda: os.system("cls")


# GUI FUNCTIONS

def gui_header():
    print("==================================================")
    print("File Encryptor")
    print("==================================================")
    print("")


def gui_choice():
    print("(1) Encrypt a file")
    print("(2) Decrypt a file")
    print("------------------")
    print("(0) Exit")
    print("")


# INPUT HANDLING FUNCTIONS

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


# ENCRYPTION / DECRYPTION  FUNCTIONS

def encrypt():
    file_name = input("File name or path > ").replace("\"", "")
    print("")
    password = input("/!\\ WARNING, PASSWORD CANNOT BE RECOVERED /!\\ ""\nPassword > ")

    success = False

    if file_name.__contains__(".aes"):
        print("")
        input("Oops, you cannot choose an encrypted file !\nPress Enter to continue... ")

    else:
        if password is not None and file_name is not None:
            buffer_size = 64 * 1024
            with open(file_name, "rb") as fIn:
                with open(file_name + ".aes", "wb") as fOut:
                    print("")
                    print("Please wait during encryption...")
                    Aes.encryptStream(fIn, fOut, password, buffer_size)
                    print("")
                    print("Encryption done !")
                    success = True

    if success:
        r = bool_input("Remove original file ? (Default N) Y or N > ", False)
        if r:
            os.remove(file_name)


def decrypt():
    file_name = input("File name or path > ").replace("\"", "")
    password = input("Password > ")

    file_extension = file_name[-3:]
    buffer_size = 64 * 1024

    success = False
    if file_extension == "aes":
        new_file_name = file_name.replace(".aes", "")
        enc_file_size = os.stat(file_name).st_size
        try:
            with open(file_name, "rb") as fIn:
                with open(new_file_name, "wb") as fOut:
                    # decrypt file stream
                    print("")
                    print("Please wait during decryption...")
                    Aes.decryptStream(fIn, fOut, password, buffer_size, enc_file_size)
                    print("")
                    print("Decryption done !")
                    success = True
        except ValueError:
            input("Oops, an error as occurred, maybe a wrong password ?\nPress Enter to continue... ")

        if success:
            r = bool_input("Remove encrypted file ? (Default No) Y or N > ", False)
            if r:
                os.remove(file_name)

    else:
        input("Oops, invalid file, choose a .aes file !\nPress Enter to continue... ")


# =========
# MAIN CODE
# =========

while True:

    clear()
    gui_header()
    gui_choice()

    c = input("Choice > ")
    print("")
    print("")

    if c == "1":
        encrypt()

    if c == "2":
        decrypt()

    if c == "0":
        break
