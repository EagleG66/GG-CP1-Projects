#>>>>>>>>>>>>>>>>>>>VARIABLES<<<<<<<<<<<<<<<<<<<<

# variable types

snake_case = "Type of var name, used for variables"

camelCase = "Type of var name, used for functions"

PascalCase = "Type of var name, used for classes"

#>>>>>>>>>>>>>>>>DEBUGGING<<<<<<<<<<<<<<<<<

# Syntax errors
error = "pritn()"

# Logic errors
apples = 20
people = 3
# how many apples each person can have
print(apples * people)

# Runtime errors
num = 5
print(num)

#>>>>>>>>>>>>>>>>>>>>>>>>>>TRY AND EXCEPT<<<<<<<<<<<<<<<<<<<<<<<
while True:
    try:
        fav_num = int(input("What is ur fav number?"))
    except:
        print("THAT'S NOT A NUMBER!!!")
    else:
        break

print(fav_num + 5)


#>>>>>>>>>>>>>>>SOFTWARE DEVELOPMENT<<<<<<<<<<<<<<

#Steps

requirement_analysis = "Understand what the program needs to be"
planning_and_design = "Map out the program"
implementation = "Write the code"
testing = "Check for errors"
release_and_maintenance = "Share the program and continue updating it"


#>>>>>>>>>>>>>>>>>INTEGERS/FLOATS<<<<<<<<<<<<<<<<<<<

integer = "A whole number"

float = "Number with a decimal"

modulo = "Returns the remainder of a division problem ===> % "


# >>>>>>>>>>>>>>>>>>DATA TYPE CONVERSION<<<<<<<<<<<<<<<<<

string = "str(number)"

string = "float(number)"

integer = "int(number)"

round = "round(number, decimal places)"


#>>>>>>>>>>>>>>>>>>STRINGS<<<<<<<<<<<<<<<<<<<<

escape_character = "\"(ignore next character)"
new_line = "\n"
tab = "\t"


sentence = "The quick brown fox jumps over the lazy dog"

# Find a thing
print(sentence.find("w"))

print(sentence[0:5])

print(len("supercalifragilisticexpialidocious"))

#>>>>>>>>>>>>>>>>>>STRING METHODS<<<<<<<<<<<<<<<

#Note: Methods do not change the string permanently

sentence = "The quick brown fox jumps over the lazy dog"


#IDOIT PROOF

# splits up the names into words and then joins them:

first_name = input("WHAT IS YOUR FIRST NAME: ").strip().split()

last_name = input("WHAT IS YOUR LAST NAME: ").strip().split()

full_name = "Hello " + "".join(first_name).title() + " " + "".join(last_name).title()

print(full_name)

print(full_name.isalpha)
print(full_name.isnumeric)
print(full_name.isupper)


# DOT NOTATION

# lowercase for every character
print(sentence.lower())

# uppercase for every character
print(sentence.upper())

# capitalize first word
print(sentence.capitalize())

# capitalize all words
print(sentence.title())

# replace x with y
print(sentence.replace("fox", "wolf"))

# splits the sentence into words
print(sentence.split())







# VOCABULARY

white_space = "indentaion or empty space"

string = "collection of any character in quotation marks"

concatenation = "adding something in a string directly after something===> print(integer + float)"

index = "Where in the string"
