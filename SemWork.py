import sys
DEFAULT_FILENAME = 'test.pbm'
DEFAULT_INPUT = 'output.pbm'
DEFAULT_MESSAGE = 'ABC'


def verify_input(input_str):
    try:
        assert (input_str == '1' or input_str == '2')
    except AssertionError:
        print("Invalid input.")
        sys.exit()


def generate_test_image():
    with open(DEFAULT_FILENAME, 'bw') as file:
        file.write(b'P4\n')
        file.write(b'5 12\n')
        file.write(b'test_content\n')


def get_source(src, significant=8):
    source = []
    for x in src:
        line = bin(ord(x))[2:]
        line = [int(x) for x in line]
        source.append(line[:significant])
    return source


def get_bitmap(filename=DEFAULT_FILENAME):
    with open(filename) as file:
        lines = file.readlines()
        significant = lines[1].split()[0]
        source = lines[-1].split()[0]
    return get_source(source, int(significant))


divide = lambda lst, sz: [lst[i:i + sz] for i in range(0, len(lst), sz)]


def get_msg_map(msg, item_len):
    msg = get_source(msg, 8, False)
    msg_unformatted = []
    for item in msg:
        for x in item:
            msg_unformatted.append(x)

    return divide(msg_unformatted, 8 - item_len % 8)


def write_output(src):
    with open("output.pbm", 'bw') as file:
        file.write(b'P4\n')
        file.write(b'5 12\n')
        for row in src:
            line = ''
            for x in row[:8:]:
                line += str(x)
            file.write(bytearray([int(line, 2)]))


def encrypt(src, message=DEFAULT_MESSAGE):
    message = get_msg_map(message, len(src[0]))
    empty = [0, 0, 0]
    res = []
    for i in range(len(src)):
        try:
            res.append(src[i] + message[i])
        except IndexError:
            res.append(src[i] + empty)

    return res


def decrypt():
    with open(DEFAULT_INPUT) as file:
        lines = file.readlines()

    source = []
    for x in lines[-1]:
        line = bin(ord(x))[2:]
        line = [int(x) for x in line]
        source.append(line[-3:])

    msg_unf = ""
    for item in source:
        for x in item:
            msg_unf += str(x)

    msg = divide(msg_unf, 7)

    print("Decryted message:")
    for it in msg:
        if int(it, 2) != 0:
            print(chr(int(it, 2)), end='')


# mode = input("Please, choose mode:\n"
#              "1. Encrypt message to PNM P4 picture.\n"
#              "2. Decrypt message from PNM P4 picture.\n"
#              "[1/2]?\t")
#
# verify_input(mode)

generate_test_image()
bitmap = get_bitmap()

mode = '1'
if mode == '2':
    write_output(encrypt(bitmap))
else:
    decrypt()

