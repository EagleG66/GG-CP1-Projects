# GLENN GUDMUNSON flexible calculator

numbers = []

def calculator(type, *args):

    total = 0 # sets up a variable to modify

    if type == "sum":                   #SUM
        total = sum(args)
        return total 
                                        #AVG
    elif type == "average":
        total = sum(args)/len(args)
        return total 
                                        #MIN
    elif type == "minimum":
        total = min(args)
        return total 
                                        #MAX
    elif type == "maximum":
        total = max(args)
        return total 
                                        #PRODUCT
    elif type == "product":
        total = 1
        for item in args:
            total *= item
        return total 
                                        #STUPID-PROOFING
    else:
        return False




while True:
    while True:
        operation = input("\nWhat operation would you like to use?(sum, average, minimum, maximum, product): ").lower()      #<<<<<<<<< Getting the operation
        print("\nPut the numbers you want to use down below and type any letter if you are done:")

        while True:
            try:                                                                #<<<<<<<< loop to get all wanted numbers from user
                num = int(input("\t- "))
                numbers.append(num)
            except:
                break


        if calculator(operation, *numbers):
            print(f"\nYour final value is: {calculator(operation, *numbers)}")      #<<<<< printing the final value
            break
        else:
            print("\nThat is not one of the available operations. Please try again")    # <<<< Stupid-proofing


    if input("\nIf you would like to do another operation, press ENTER. If not, type something and press ENTER: "):  #<<<<<Checking to see if they want to do another calculation
        break

