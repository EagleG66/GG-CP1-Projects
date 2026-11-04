# caesar cipher GLENN GUDMUNSON

caesar_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
bad_char = False

#encode function
def cipherEncode(letter):

    """This function sets each letter of the alphabet to the new letter, depending on what the shift is. It does this positively, and then returns the letter"""

    caesar_list1 = {
        "a": caesar_list[(0 + shift) % 26], 
        "b": caesar_list[(1 + shift) % 26], 
        "c": caesar_list[(2 + shift) % 26], 
        "d": caesar_list[(3 + shift) % 26], 
        "e": caesar_list[(4 + shift) % 26], 
        "f": caesar_list[(5 + shift) % 26], 
        "g": caesar_list[(6 + shift) % 26], 
        "h": caesar_list[(7 + shift) % 26], 
        "i": caesar_list[(8 + shift) % 26], 
        "j": caesar_list[(9 + shift) % 26], 
        "k": caesar_list[(10 + shift) % 26], 
        "l": caesar_list[(11 + shift) % 26], 
        "m": caesar_list[(12 + shift) % 26], 
        "n": caesar_list[(13 + shift) % 26], 
        "o": caesar_list[(14 + shift) % 26], 
        "p": caesar_list[(15 + shift) % 26], 
        "q": caesar_list[(16 + shift) % 26], 
        "r": caesar_list[(17 + shift) % 26], 
        "s": caesar_list[(18 + shift) % 26], 
        "t": caesar_list[(19 + shift) % 26], 
        "u": caesar_list[(20 + shift) % 26], 
        "v": caesar_list[(21 + shift) % 26], 
        "w": caesar_list[(22 + shift) % 26], 
        "x": caesar_list[(23 + shift) % 26], 
        "y": caesar_list[(24 + shift) % 26], 
        "z": caesar_list[(25 + shift) % 26]
    }

    if letter.lower() in caesar_list1:
        return caesar_list1[letter.lower()]

#decode function
def cipherDecode(letter):
    """This function sets each letter of the alphabet to the new letter, depending on what the shift is. It does this negatively, and then returns the letter"""
    caesar_list1 = {
        "a": caesar_list[(0 - shift) % 26], 
        "b": caesar_list[(1 - shift) % 26], 
        "c": caesar_list[(2 - shift) % 26], 
        "d": caesar_list[(3 - shift) % 26], 
        "e": caesar_list[(4 - shift) % 26], 
        "f": caesar_list[(5 - shift) % 26], 
        "g": caesar_list[(6 - shift) % 26], 
        "h": caesar_list[(7 - shift) % 26], 
        "i": caesar_list[(8 - shift) % 26], 
        "j": caesar_list[(9 - shift) % 26], 
        "k": caesar_list[(10 - shift) % 26], 
        "l": caesar_list[(11 - shift) % 26], 
        "m": caesar_list[(12 - shift) % 26], 
        "n": caesar_list[(13 - shift) % 26], 
        "o": caesar_list[(14 - shift) % 26], 
        "p": caesar_list[(15 - shift) % 26], 
        "q": caesar_list[(16 - shift) % 26], 
        "r": caesar_list[(17 - shift) % 26], 
        "s": caesar_list[(18 - shift) % 26], 
        "t": caesar_list[(19 - shift) % 26], 
        "u": caesar_list[(20 - shift) % 26], 
        "v": caesar_list[(21 - shift) % 26], 
        "w": caesar_list[(22 - shift) % 26], 
        "x": caesar_list[(23 - shift) % 26], 
        "y": caesar_list[(24 - shift) % 26], 
        "z": caesar_list[(25 - shift) % 26]
    }

    if letter.lower() in caesar_list1:
        return caesar_list1[letter.lower()]

while True:
    try:
        code = int(input("Would you like to encode(type 1) or decode(type 2) the message: "))
    except:
        print("That is not a number. Please try again")
    else:
        if code == 1 or code == 2:
            break
        else:
            print("That is not one of the options. Please try again")



while True:
    try:
        shift = int(input("What shift value would you like: "))
    except:
        print("That is not a number. Please try again")
    else:
        break

while True:
    try:
        words = input("what letters would you like to encode(only use normal letters, no special characters): ")
    except:
        pass
    else:
        for letter in list(words):
            if letter in caesar_list:
                pass
            else:
                bad_char = True
                break
        if bad_char:
            break


if code == 1:
    shifted_list = map(cipherEncode, list(words))
elif code == 2:
    shifted_list = map(cipherDecode, list(words))

print(f"Your encoded word is {"".join(shifted_list)}")
