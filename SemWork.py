import sys
mode = input("Please, choose mode:\n"
             "1. Encrypt message to PNM P4 picture.\n"
             "2. Decrypt message from PNM P4 picture.\n"
             "[1/2]?\t")

try:
    assert (mode == '1' or mode == '2')
except AssertionError as ex:
    print("Invalid input.")
    sys.exit()

