# GLENN GUDMUNSON factorial

big_num = 1

def factorial(number):
    big_num = number * big_num

while True:
    try:
        input_num = int(input("What number do you want the factorial for(must be negative): "))
    except:
        print("That is not a number. Please try again")
    else:
        if input_num <= 0:
            print("Your number must be positive. Please try again")
        else:
            break

factorial_nums = map(factorial, range(1, input_num + 1))

print(f"Your final number is {big_num}")