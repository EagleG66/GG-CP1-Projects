# GLENN GUDMUNSON factorial
import math as m
big_num = 1

def func(number):
    return number

while True:
    try:
        input_num = int(input("What number do you want the factorial for(must be positive): "))
    except:
        print("That is not a number. Please try again")
    else:
        if input_num <= 0:
            print("Your number must be positive. Please try again")
        else:
            break

factorial_nums = map(func, range(1, input_num + 1))
num_list = list(factorial_nums)

print(num_list[0], end="")

for i in num_list:
    print(f" x {num_list[i-1]}", end="")
print(f" = {m.factorial(input_num)}")