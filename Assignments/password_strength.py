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


if len(password) >= 8:
    score += 1

for i in password:
    if i.isupper():
        upper = True
    if i.islower():
        lower = True
    if i.isnumeric():
        number = True
    if ord(i) == 33 or (ord(i) >= 35 and ord(i) <= 38) or (ord(i) >= 40 and ord(i) <= 46) or (ord(i) >= 58 and ord(i) <= 64) or (ord(i) == 91) or (ord(i) >= 93 and ord(i) <= 95) or (ord(i) >= 123 and ord(i) <= 125):
        special_char = True


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


