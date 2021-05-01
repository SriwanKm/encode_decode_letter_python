# Proj01 - Encode/Decode Letter
# Sriwan Khaomuang
# coding=utf-8

# variable declaration
FINAL_ALPHABETIC_ORDINAL_PLUS_ONE = 123
INITIAL_ALPHABETIC_ORDINAL = 97
MIN_ROTATIONS = 1
MAX_ROTATIONS = 25
WHITESPACE_ORDINAL = 32
WHITESPACE = " "


def greeting():
    print("""
    ╭╮╭╮╭┳━━━┳╮╱╱╭━━━┳━━━┳━╮╭━┳━━━╮
    ┃┃┃┃┃┃╭━━┫┃╱╱┃╭━╮┃╭━╮┃┃╰╯┃┃╭━━╯
    ┃┃┃┃┃┃╰━━┫┃╱╱┃┃╱╰┫┃╱┃┃╭╮╭╮┃╰━━╮
    ┃╰╯╰╯┃╭━━┫┃╱╭┫┃╱╭┫┃╱┃┃┃┃┃┃┃╭━━╯
    ╰╮╭╮╭┫╰━━┫╰━╯┃╰━╯┃╰━╯┃┃┃┃┃┃╰━━╮
    ╱╰╯╰╯╰━━━┻━━━┻━━━┻━━━┻╯╰╯╰┻━━━╯""")
    start = input("To start the program type e to encode, d to decode, or q to quit: ")
    start_input(start)


def start_input(start):
    if start == "q":
        print("""
███████████████████████████████████████
█▄─▄─▀█▄─█─▄█▄─▄▄─███▄─▄─▀█▄─█─▄█▄─▄▄─█
██─▄─▀██▄─▄███─▄█▀████─▄─▀██▄─▄███─▄█▀█
▀▄▄▄▄▀▀▀▄▄▄▀▀▄▄▄▄▄▀▀▀▄▄▄▄▀▀▀▄▄▄▀▀▄▄▄▄▄▀""")
        return

    elif start == "e":
        to_encode()
        start = input("Type e to encode, d to decode, or q to quit: ")
        start_input(start)

    elif start == "d":
        to_decode()
        start = input("Type e to encode, d to decode, or q to quit: ")
        start_input(start)

    else:
        start = input("Type e to encode, d to decode, or q to quit: ")
        start_input(start)


def to_encode():
    e = input("What's the text you want to encode: ")
    rotation = int(input("Enter a rotation number: "))
    # mapping the input(e) and feed each letter into the function encode_letter
    # the result of function encode_letter come out in the form of an object so we turn it back into array using list()
    # then join the array to get string format
    if rotation < MIN_ROTATIONS or rotation > MAX_ROTATIONS:
        print("The rotation is out of range")
    else:
        print("Your encoded text is:", "".join(list(map(lambda x: encode_letter(x, rotation), e))))


def to_decode():
    d = input("What's the text you want to decode: ")
    decoded_word = input("Enter a decoded word in the letter: ")
    # mapping the input(d) and feed each letter into the function decode_letter
    # the result of function decode_letter come out in the form of an object so we turn it back into array using list()
    # then join the array to get string format
    decoded_letter, shift = find_rotation(d, decoded_word)

    print("The rotation is", shift)
    message = "Your Original Word: " + d if shift == "not found" or\
        shift == 0 else "Your decoded text is: " + decoded_letter
    print(message)


def encode_letter(letter, rotation):
    new_ordinal = ord(letter) + rotation
    # get ordinal number of the letter and rotate

    if letter == WHITESPACE:
        new_ordinal = WHITESPACE_ORDINAL
        # if the letter is a whitespace remain the same

    elif ord(letter) < INITIAL_ALPHABETIC_ORDINAL or ord(letter) >= FINAL_ALPHABETIC_ORDINAL_PLUS_ONE:
        new_ordinal = ord(letter)

    elif new_ordinal >= FINAL_ALPHABETIC_ORDINAL_PLUS_ONE:
        new_ordinal = new_ordinal % FINAL_ALPHABETIC_ORDINAL_PLUS_ONE + INITIAL_ALPHABETIC_ORDINAL
        # after rotating if the order number over the letter "z" then using mod to start with letter "a" again

    return chr(new_ordinal)


def rotate(old_str, rotation):
    new_str = ""
    for letter in old_str:
        if letter == " " or ord(letter) < INITIAL_ALPHABETIC_ORDINAL or ord(letter) >= FINAL_ALPHABETIC_ORDINAL_PLUS_ONE:
            new_str += letter
        elif ord(letter) + rotation >= FINAL_ALPHABETIC_ORDINAL_PLUS_ONE:
            letter = (ord(letter) + rotation) % FINAL_ALPHABETIC_ORDINAL_PLUS_ONE + INITIAL_ALPHABETIC_ORDINAL
            new_str += chr(letter)
        else:
            new_letter = chr(ord(letter) + rotation)
            new_str += new_letter
    return new_str


def find_rotation(test_string, keyword):
    if keyword in test_string:
        return test_string, 0

    for num in range(1, 26):

        variation = rotate(test_string, num)
        if keyword in variation:
            return variation, num
    return test_string, "not found"


greeting()
