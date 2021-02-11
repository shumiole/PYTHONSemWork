import sys
DEFAULT_FILENAME = 'test.pbm'
DEFAULT_MESSAGE = 'SECRET'


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


def get_source(src, append_zero=True):
    source = []
    for x in src:
        line = bin(ord(x))[2:]
        line = [int(x) for x in line]
        while append_zero and len(line) < 8:
            line.insert(0, 0)
        source.append(line)
    return source


def get_bitmap(filename=DEFAULT_FILENAME):
    with open(filename) as file:
        source = file.readlines()[-1].split()[0]
    return get_source(source)


def delete_irrelevant(src):
    delta = len(src[0]) - (len(src[0]) % 8)
    if delta != len(src[0]):
        normalized = []
        for row in src:
            normalized.append(row[:delta:])
        return normalized
    else:
        return src


def get_msg_map(msg, src_len):
    empty = [0, 0, 0, 0, 0, 0, 0]
    msg = get_source(msg, False)
    while len(msg) < src_len:
        msg.append(empty)
    return msg


def write_output(src):
    pass


def encrypt(src, message=DEFAULT_MESSAGE):
    src = delete_irrelevant(src)
    message = get_msg_map(message, len(src))
    res = []
    for i in range(len(src)):
        res.append(src[i] + message[i])
    return res


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

mode = '1'
if mode == '1':
    write_output(encrypt(bitmap))
else:
    decrypt()

