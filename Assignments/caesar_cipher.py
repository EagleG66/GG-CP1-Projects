# caesar cipher GLENN GUDMUNSON


def encode(character):
    if ord(character) >= 97 and ord(character) <= 122:
        new_letter = chr(ord(character) + (shift % 26))
    elif ord(character) >= 65 and ord(character) <= 90:
        new_letter = chr(ord(character) + (shift % 26))
    else:
        new_letter = character

    return new_letter


def decode(character):
    if ord(character) >= 97 and ord(character) <= 122:
        new_letter = chr(ord(character) - (shift % 26))
    elif ord(character) >= 65 and ord(character) <= 90:
        new_letter = chr(ord(character) - (shift % 26))
    else:
        new_letter = character

    return new_letter

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
        words = input("what letters would you like to encode(only use normal letters, no special characters): ").lower()
    except:
        pass
    else:
        break


if code == 1:
    shifted_list = map(encode, list(words))
elif code == 2:
    shifted_list = map(decode, list(words))

print(f"Your ending word is {"".join(shifted_list)}")




