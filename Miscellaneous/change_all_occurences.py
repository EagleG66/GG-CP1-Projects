def cipherDecode(letter):

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