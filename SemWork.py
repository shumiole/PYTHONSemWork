import sys


def verify_input(input_str):
    try:
        assert (input_str == '1' or input_str == '2')
    except AssertionError:
        print("Invalid input.")
        sys.exit()


def encrypt():
    pass


def decrypt():
    pass


mode = input("Please, choose mode:\n"
             "1. Encrypt message to PNM P4 picture.\n"
             "2. Decrypt message from PNM P4 picture.\n"
             "[1/2]?\t")

verify_input(mode)

if mode == '1':
    encrypt()
else:
    decrypt()

