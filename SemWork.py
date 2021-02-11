import sys
import numpy as np
DEFAULT_FILENAME = 'test.pbm'


def verify_input(input_str):
    try:
        assert (input_str == '1' or input_str == '2')
    except AssertionError:
        print("Invalid input.")
        sys.exit()


def generate_test_image():
    with open(DEFAULT_FILENAME, 'bw') as file:
        file.write(b'P4\n')
        file.write(b'8 12\n')
        file.write(b'test_content\n')


def get_bitmap(filename=DEFAULT_FILENAME):
    with open(filename) as file:
        raw_source = file.readlines()[-1].split()[0]
    source = []
    for x in raw_source:
        line = bin(ord(x))[2:]
        line = [int(x) for x in line]
        while len(line) < 8:
            line.insert(0, 0)
        source.append(line)
    return np.matrix(source)


def encrypt():
    pass


def decrypt():
    pass


# mode = input("Please, choose mode:\n"
#              "1. Encrypt message to PNM P4 picture.\n"
#              "2. Decrypt message from PNM P4 picture.\n"
#              "[1/2]?\t")
#
# verify_input(mode)

generate_test_image()
bitmap = get_bitmap()
print(bitmap)

# if mode == '1':
#     encrypt()
# else:
#     decrypt()

