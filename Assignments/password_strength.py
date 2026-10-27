#GLENN GUDMUNSON password strength checker

score = 0
upper = False
lower = False
number = False
special_char = False

print("\t\t\t------PASSWORD STRENGTH CHECKER------")
print("\n\t\t\tDuring this check, we will check for:")
print("\t\t\t- 8 characters")
print("\t\t\t- any uppercase letters")
print("\t\t\t- any lowercase letters")
print("\t\t\t- any numbers")
print("\t\t\t- any special characters")

password = list(input("\nPlease type in the password you would like to test: "))

def uppercase(character):
    if character.isupper():
        upper = True

def lowercase(character):
    if character.islower():
        lower = True

def numerical(character):
    if character.isnumeric():
        number = True

def special(character):
    if ord(character) == 33 or (ord(character) >= 35 and ord(character) <= 38) or (ord(character) >= 40 and ord(character) <= 46) or (ord(character) >= 58 and ord(character) <= 64) or (ord(character) == 91) or (ord(character) >= 93 and ord(character) <= 95) or (ord(character) >= 123 and ord(character) <= 125):
        special_char = True

if len(password) >= 8:
    score += 1

for i in password:
    uppercase(i)

for i in password:
    lowercase(i)

for i in password:
    numerical(i)

for i in password:
    special(i)


if upper:
    score += 1

if lower:
    score += 1

if number:
    score += 1

if special_char:
    score += 1

if score == 5:
	strength = "Very Strong"
elif score == 4:
	strength = "Strong"
elif score == 3:
	strength = "Moderate"
elif score == 1 or score == 2:
	strength = "Weak"
elif score == 0:
    strength = "Unbelievably Terrible"

print(f"Strength Score: {score}/5")
print(f"Overall Strength: {strength}")


