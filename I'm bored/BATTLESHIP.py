import time

#>>>>>>>>>>>>>VARIABLES<<<<<<<<<<<


# Player 2 board spaces

A = [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
B = [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]

p1_ship_coords = []
p2_ship_coords = []


p1_turn = False
p2_turn = False

p1_start = True
p2_start = False






def p1GameBoard():
    print(f"     1         2         3         4         5         6         7         8         9         10   ")
    print(f"          |         |         |         |         |         |         |         |         |         ")
    print(f"A    {A[1]}    |    {A[2]}    |    {A[3]}    |    {A[4]}    |    {A[5]}    |    {A[6]}    |    {A[7]}    |    {A[8]}    |    {A[9]}    |    {A[10]}    ")
    print(f"          |         |         |         |         |         |         |         |         |         ")
    print(f" ---------+---------+---------+---------+---------+---------+---------+---------+---------+---------")
    print(f"          |         |         |         |         |         |         |         |         |         ")
    print(f"B    {A[11]}    |    {A[12]}    |    {A[13]}    |    {A[14]}    |    {A[15]}    |    {A[16]}    |    {A[17]}    |    {A[18]}    |    {A[19]}    |    {A[20]}    ")
    print(f"          |         |         |         |         |         |         |         |         |         ")
    print(f" ---------+---------+---------+---------+---------+---------+---------+---------+---------+---------")
    print(f"          |         |         |         |         |         |         |         |         |         ")
    print(f"C    {A[21]}    |    {A[22]}    |    {A[23]}    |    {A[24]}    |    {A[25]}    |    {A[26]}    |    {A[27]}    |    {A[28]}    |    {A[29]}    |    {A[30]}    ")
    print(f"          |         |         |         |         |         |         |         |         |         ")
    print(f" ---------+---------+---------+---------+---------+---------+---------+---------+---------+---------")
    print(f"          |         |         |         |         |         |         |         |         |         ")
    print(f"D    {A[31]}    |    {A[32]}    |    {A[33]}    |    {A[34]}    |    {A[35]}    |    {A[36]}    |    {A[37]}    |    {A[38]}    |    {A[39]}    |    {A[40]}    ")
    print(f"          |         |         |         |         |         |         |         |         |         ")
    print(f" ---------+---------+---------+---------+---------+---------+---------+---------+---------+---------")
    print(f"          |         |         |         |         |         |         |         |         |         ")
    print(f"E    {A[41]}    |    {A[42]}    |    {A[43]}    |    {A[44]}    |    {A[45]}    |    {A[46]}    |    {A[47]}    |    {A[48]}    |    {A[49]}    |    {A[50]}    ")
    print(f"          |         |         |         |         |         |         |         |         |         ")
    print(f" ---------+---------+---------+---------+---------+---------+---------+---------+---------+---------")
    print(f"          |         |         |         |         |         |         |         |         |         ")
    print(f"F    {A[51]}    |    {A[52]}    |    {A[53]}    |    {A[54]}    |    {A[55]}    |    {A[56]}    |    {A[57]}    |    {A[58]}    |    {A[59]}    |    {A[60]}    ")
    print(f"          |         |         |         |         |         |         |         |         |         ")
    print(f" ---------+---------+---------+---------+---------+---------+---------+---------+---------+---------")
    print(f"          |         |         |         |         |         |         |         |         |         ")
    print(f"G    {A[61]}    |    {A[62]}    |    {A[63]}    |    {A[64]}    |    {A[65]}    |    {A[66]}    |    {A[67]}    |    {A[68]}    |    {A[69]}    |    {A[70]}    ")
    print(f"          |         |         |         |         |         |         |         |         |         ")
    print(f" ---------+---------+---------+---------+---------+---------+---------+---------+---------+---------")
    print(f"          |         |         |         |         |         |         |         |         |         ")
    print(f"H    {A[71]}    |    {A[72]}    |    {A[73]}    |    {A[74]}    |    {A[75]}    |    {A[76]}    |    {A[77]}    |    {A[78]}    |    {A[79]}    |    {A[80]}    ")
    print(f"          |         |         |         |         |         |         |         |         |         ")
    print(f" ---------+---------+---------+---------+---------+---------+---------+---------+---------+---------")
    print(f"          |         |         |         |         |         |         |         |         |         ")
    print(f"I    {A[81]}    |    {A[82]}    |    {A[83]}    |    {A[84]}    |    {A[85]}    |    {A[86]}    |    {A[87]}    |    {A[88]}    |    {A[89]}    |    {A[90]}    ")
    print(f"          |         |         |         |         |         |         |         |         |         ")
    print(f" ---------+---------+---------+---------+---------+---------+---------+---------+---------+---------")
    print(f"          |         |         |         |         |         |         |         |         |         ")
    print(f"J    {A[91]}    |    {A[92]}    |    {A[93]}    |    {A[94]}    |    {A[95]}    |    {A[96]}    |    {A[97]}    |    {A[98]}    |    {A[99]}    |    {A[100]}    ")
    print(f"          |         |         |         |         |         |         |         |         |         ")



def p1GameBoard():
    print(f"     1         2         3         4         5         6         7         8         9         10   ")
    print(f"          |         |         |         |         |         |         |         |         |         ")
    print(f"A    {B[1]}    |    {B[2]}    |    {B[3]}    |    {B[4]}    |    {B[5]}    |    {B[6]}    |    {B[7]}    |    {B[8]}    |    {B[9]}    |    {B[10]}    ")
    print(f"          |         |         |         |         |         |         |         |         |         ")
    print(f" ---------+---------+---------+---------+---------+---------+---------+---------+---------+---------")
    print(f"          |         |         |         |         |         |         |         |         |         ")
    print(f"B    {B[11]}    |    {B[12]}    |    {B[13]}    |    {B[14]}    |    {B[15]}    |    {B[16]}    |    {B[17]}    |    {B[18]}    |    {B[19]}    |    {B[20]}    ")
    print(f"          |         |         |         |         |         |         |         |         |         ")
    print(f" ---------+---------+---------+---------+---------+---------+---------+---------+---------+---------")
    print(f"          |         |         |         |         |         |         |         |         |         ")
    print(f"C    {B[21]}    |    {B[22]}    |    {B[23]}    |    {B[24]}    |    {B[25]}    |    {B[26]}    |    {B[27]}    |    {B[28]}    |    {B[29]}    |    {B[30]}    ")
    print(f"          |         |         |         |         |         |         |         |         |         ")
    print(f" ---------+---------+---------+---------+---------+---------+---------+---------+---------+---------")
    print(f"          |         |         |         |         |         |         |         |         |         ")
    print(f"D    {B[31]}    |    {B[32]}    |    {B[33]}    |    {B[34]}    |    {B[35]}    |    {B[36]}    |    {B[37]}    |    {B[38]}    |    {B[39]}    |    {B[40]}    ")
    print(f"          |         |         |         |         |         |         |         |         |         ")
    print(f" ---------+---------+---------+---------+---------+---------+---------+---------+---------+---------")
    print(f"          |         |         |         |         |         |         |         |         |         ")
    print(f"E    {B[41]}    |    {B[42]}    |    {B[43]}    |    {B[44]}    |    {B[45]}    |    {B[46]}    |    {B[47]}    |    {B[48]}    |    {B[49]}    |    {B[50]}    ")
    print(f"          |         |         |         |         |         |         |         |         |         ")
    print(f" ---------+---------+---------+---------+---------+---------+---------+---------+---------+---------")
    print(f"          |         |         |         |         |         |         |         |         |         ")
    print(f"F    {B[51]}    |    {B[52]}    |    {B[53]}    |    {B[54]}    |    {B[55]}    |    {B[56]}    |    {B[57]}    |    {B[58]}    |    {B[59]}    |    {B[60]}    ")
    print(f"          |         |         |         |         |         |         |         |         |         ")
    print(f" ---------+---------+---------+---------+---------+---------+---------+---------+---------+---------")
    print(f"          |         |         |         |         |         |         |         |         |         ")
    print(f"G    {B[61]}    |    {B[62]}    |    {B[63]}    |    {B[64]}    |    {B[65]}    |    {B[66]}    |    {B[67]}    |    {B[68]}    |    {B[69]}    |    {B[70]}    ")
    print(f"          |         |         |         |         |         |         |         |         |         ")
    print(f" ---------+---------+---------+---------+---------+---------+---------+---------+---------+---------")
    print(f"          |         |         |         |         |         |         |         |         |         ")
    print(f"H    {B[71]}    |    {B[72]}    |    {B[73]}    |    {B[74]}    |    {B[75]}    |    {B[76]}    |    {B[77]}    |    {B[78]}    |    {B[79]}    |    {B[80]}    ")
    print(f"          |         |         |         |         |         |         |         |         |         ")
    print(f" ---------+---------+---------+---------+---------+---------+---------+---------+---------+---------")
    print(f"          |         |         |         |         |         |         |         |         |         ")
    print(f"I    {B[81]}    |    {B[82]}    |    {B[83]}    |    {B[84]}    |    {B[85]}    |    {B[86]}    |    {B[87]}    |    {B[88]}    |    {B[89]}    |    {B[90]}    ")
    print(f"          |         |         |         |         |         |         |         |         |         ")
    print(f" ---------+---------+---------+---------+---------+---------+---------+---------+---------+---------")
    print(f"          |         |         |         |         |         |         |         |         |         ")
    print(f"J    {B[91]}    |    {B[92]}    |    {B[93]}    |    {B[94]}    |    {B[95]}    |    {B[96]}    |    {B[97]}    |    {B[98]}    |    {B[99]}    |    {B[100]}    ")
    print(f"          |         |         |         |         |         |         |         |         |         ")


def place_ship(length, player):

    while True:
        try:
            coordinate = input(f"Place your Carrier({length} spaces long) by entering the first coordinate(example: C3): ").title().strip()
            coordinates_list = list(coordinate)
            row_value = ord(coordinates_list[0])

            if len(coordinates_list) == 3:
                rlist = [coordinates_list[1], coordinates_list[2]]
                column = "".join(rlist)
            else:
                column = coordinates_list[1]
            
            column_num = int(column)

        except:
            print("That is not an option!!!")
        else:
            if len(coordinate) >= 2 and len(coordinate) <= 3 and column_num >= 1 and column_num <= 10 and row_value >= 65 and row_value <= 74:
                row_value -= 65
                row_value = row_value * 10
                start_coord = row_value + column_num
                break
            else:
                print("THAT'S NOT AN OPTION!!!")

    # End coordinate (five long)
    while True:
        try:
            direction = input("Finish placing your carrier by entering the direction you want it to face(R for right, L for left, U for up, D for down): ").strip().capitalize()
        except:
            print("THAT'S NOT AN OPTION!!!")
        else:

            #RIGHT

            if direction == "R":
                end_coord = row_value + column_num + (length - 1)
                start_list = list(str(start_coord))
                end_list = list(str(end_coord))

                if len(start_list) == 1 and len(end_list) == 1:
                    start_num = 0
                    end_num = 0
                elif len(start_list) == 1 and len(end_list) == 2:
                    start_num = 0
                    end_num = end_list[0]
                elif len(start_list) == 1 and len(end_list) == 2:
                    start_num = start_list[0]
                    end_num = 0
                elif len(start_list) == 2 and len(end_list) == 2:
                    start_num = start_list[0]
                    end_num = end_list[0]


                if end_num == start_num:
                    if player == 1:
                        p1_ship_coords.append(start_coord)
                        p1_ship_coords.append(start_coord + 1)
                        if length > 2:
                            p1_ship_coords.append(start_coord + 2)
                        if length > 3:
                            p1_ship_coords.append(start_coord + 3)
                        if length > 4:
                            p1_ship_coords.append(start_coord + 4)
                    elif player == 2:
                        p2_ship_coords.append(start_coord)
                        p2_ship_coords.append(start_coord + 1)
                        if length > 2:
                            p2_ship_coords.append(start_coord + 2)
                        if length > 3:
                            p2_ship_coords.append(start_coord + 3)
                        if length > 4:
                            p2_ship_coords.append(start_coord + 4)
                    break
                else:
                    print("YOUR SHIP CANNOT CUT INTO THE SIDE OF THE BOARD!!!")

            #LEFT

            elif direction == "L":
                end_coord = row_value + column_num - (length - 1)
                start_list = list(str(start_coord))
                end_list = list(str(end_coord))

                if len(start_list) == 1 and len(end_list) == 1:
                    start_num = 0
                    end_num = 0
                elif len(start_list) == 1 and len(end_list) == 2:
                    start_num = 0
                    end_num = end_list[0]
                elif len(start_list) == 1 and len(end_list) == 2:
                    start_num = start_list[0]
                    end_num = 0
                elif len(start_list) == 2 and len(end_list) == 2:
                    start_num = start_list[0]
                    end_num = end_list[0]


                if end_num == start_num:
                    if player == 1:
                        p1_ship_coords.append(end_coord)
                        p1_ship_coords.append(end_coord + 1)
                        if length > 2:
                            p1_ship_coords.append(end_coord + 2)
                        if length > 3:
                            p1_ship_coords.append(end_coord + 3)
                        if length > 4:
                            p1_ship_coords.append(end_coord + 4)
                    elif player == 2:
                        p2_ship_coords.append(end_coord)
                        p2_ship_coords.append(end_coord + 1)
                        if length > 2:
                            p2_ship_coords.append(end_coord + 2)
                        if length > 3:
                            p2_ship_coords.append(end_coord + 3)
                        if length > 4:
                            p2_ship_coords.append(end_coord + 4)
                    break
                else:
                    print("YOUR SHIP CANNOT CUT INTO THE SIDE OF THE BOARD!!!")
            
            #DOWN

            elif direction == "D":
                end_coord = row_value + column_num + (4*(length - 1))
                
                if end_coord > 100 or end_coord < 0:
                    print("YOUR SHIP CANNOT CUT INTO THE SIDE OF THE BOARD!!!")
                else:
                    if player == 1:
                        p1_ship_coords.append(start_coord)
                        p1_ship_coords.append(start_coord - 10)
                        if length > 2:
                            p1_ship_coords.append(start_coord - 20)
                        if length > 3:
                            p1_ship_coords.append(start_coord - 30)
                        if length > 4:
                            p1_ship_coords.append(start_coord - 40)
                    elif player == 2:
                        p2_ship_coords.append(start_coord)
                        p2_ship_coords.append(start_coord - 10)
                        if length > 2:
                            p2_ship_coords.append(start_coord - 20)
                        if length > 3:
                            p2_ship_coords.append(start_coord - 30)
                        if length > 4:
                            p2_ship_coords.append(start_coord - 40)
                    break
                    
            #UP

            elif direction == "U":
                end_coord = row_value + column_num - (4*(length - 1))
                
                if end_coord > 100 or end_coord < 0:
                    print("YOUR SHIP CANNOT CUT INTO THE SIDE OF THE BOARD!!!")
                else:
                    if player == 1:
                        p1_ship_coords.append(start_coord)
                        p1_ship_coords.append(start_coord + 10)
                        if length > 2:
                            p1_ship_coords.append(start_coord + 20)
                        if length > 3:
                            p1_ship_coords.append(start_coord + 30)
                        if length > 4:
                            p1_ship_coords.append(start_coord + 40)
                    elif player == 2:
                        p2_ship_coords.append(start_coord)
                        p2_ship_coords.append(start_coord + 10)
                        if length > 2:
                            p2_ship_coords.append(start_coord + 20)
                        if length > 3:
                            p2_ship_coords.append(start_coord + 30)
                        if length > 4:
                            p2_ship_coords.append(start_coord + 40)
                    break
                    
            else:
                print("THAT'S NOT AN OPTION!!!")




while True:
    if p1_start:
        input("Have player 2 look away while you set up your ships, and press enter when you are ready.")
        p1GameBoard()
        place_ship(5,1)
        place_ship(4,1)
        place_ship(3,1)
        place_ship(3,1)
        place_ship(2,1)
        

# Your ships will collide so you must make it so they won't be able to put two ships in the same place...